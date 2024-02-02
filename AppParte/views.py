from http.client import HTTPResponse
from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout , authenticate # logaout espara crear la cookie de session 
from django.db import IntegrityError
import datetime 
from AppParte.admin import FechaRegistro
from .forms import parteDiarioClass
from .models import parteDiario, agente
from django.contrib.auth.decorators import login_required 
# Create your views here.



def index(request):
    encabezado= """
REGISTRO DE ASISTENCIA - PERSONAL HNUS                
"""
    return render(request,'index.html',{'encabezado':encabezado})

def salir(request):
    logout(request)
    return redirect('index')

def registrarse(request):
    if request.method=='GET':
        return render(request,'registrarse.html', {
        'form':UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            #registrar usuario
            try: 
                usuario= User.objects.create_user(username=request.POST['username'], password= request.POST['password1'])
                usuario.save()
                login(request,usuario) 
                return redirect('parte_diario')
            except IntegrityError:
                return render(request,'registrarse.html', {
                    'form':UserCreationForm,
                    'error':'El Usuario ya existe '
                })
        return render(request,'registrarse.html', {
                    'form':UserCreationForm,
                    'error':'La contraseña no coincide '
                })
    
def ingresar(request):
    if request.method == 'GET':
        return render(request, 'ingresar.html',{
            'form':AuthenticationForm,
        })
    else:
        usuario_valido=authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if usuario_valido is None:
            return render(request, 'ingresar.html',{
                'form':AuthenticationForm,
                'error':'usuario o contraseña incorrectas',
            })
        else: 
            login(request, usuario_valido)
            return redirect('parte_diario')
   
    


@login_required
def parte_diario(request):
    if request.method=='GET':
        return render(request, 'parte_diario.html',{
        'form':parteDiarioClass
    })
    else:
        try:
            formParte= parteDiarioClass(request.POST)
            nuevoParte= formParte.save(commit=False) 
            nuevoParte.usuarioIngreso = request.user
            nuevoParte.save()
            return redirect ('index')
        except ValueError:
            return render(request, 'parte_diario.html',{
            'form':parteDiarioClass,
            'error': 'Ingresar un dato valido'
        })      

@login_required
def control(request):
    fechaConsulta= datetime.date.today()
    print(fechaConsulta)
    #fechaConsulta.strftime("%X")
    datos = parteDiario.objects.all() #(ingresadoFecha=fechaConsulta)
    print (datos)
    return render (request, 'control.html', {'datos':datos})