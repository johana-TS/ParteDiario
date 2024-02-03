
(function () {
const btnEliminar= document.querySelectorAll(".btnEliminar")

btnEliminar.forEach(btn=>{
    btn.addEventListener('click', (e) => {
        const confirmacion = confirm('¿Desea eliminar el dato seleccionado?');
        if (!confirmacion){
            e.preventDefault();
        };
    }) ;

});
})();