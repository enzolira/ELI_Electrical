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
// -------------------------crear input de tablero de distribuicion--------------------


// function addTable() {
//   var tableSelect = document.getElementById("table-select");
//   var nameTdGroup = document.getElementById("name-td-group");

//   if (tableSelect.value == 1) {
//     var input = document.createElement("input");
//     input.type = "text";
//     input.className = "form-control";
//     input.placeholder = "Ingresa nombre del tablero";
//     input.name = "name_td";
//     nameTdGroup.appendChild(input);
//   } else {
//     nameTdGroup.innerHTML = "";
//   }
// }

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
          content += `<option id=${elmt.id}>${elmt.name}</option>`
        });
        tableSelect.innerHTML = content;
      }
    },
    error: (xhr, textStatus, error) => {
      console.log(xhr, textStatus, error);
    },
  });
}


  




