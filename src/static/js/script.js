// -----------------------------------------------------------------------------------
// -------------------------confirmacion de cierre de sesion ------------------------------

function confirmar(event) {
  if (!confirm('¿Estás seguro de que quieres cerrar sesión?')) {
    event.preventDefault();
  }
}

// -----------------------------------------------------------------------------------
// -------------------------agregar circuito como tabla ------------------------------

// var proyect = document.getElementById('proyect-select');
// proyect.addEventListener('change', function() {
// var proyectElegido = proyect.value;
// console.log(proyectElegido);
// });

// ------------------------------------------------------------------------------------
// -------------------------crear select con tableros generales segun proyecto --------------------

function proyect(element){
  console.log(element.value);
  $.ajax({
    url: "/api/tgs",
    method: 'POST',
    data: {proyect: element.value},
    success: (data, textStatus, xhr) => {
      console.log(data, textStatus, xhr);
      if (textStatus === 'success'){
        tableSelect = document.getElementById("td-select");
        content = '<option selected>-Seleccione Tablero-</option>';
        data.map(elmt => {
          content += `<option value=${elmt.id}>${elmt.name}</option>`
        });
        tableSelect.innerHTML = content;
      }
    },
    error: (xhr, textStatus, error) => {
      console.log(xhr, textStatus, error);
    },
  });
}


  




