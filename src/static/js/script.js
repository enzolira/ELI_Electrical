// -----------------------------------------------------------------------------------
// -------------------------CONFIRMACION CIERRE DE SESION------------------------------

function confirmar(event) {
  if (!confirm('¿Estás seguro de que quieres cerrar sesión?')) {
    event.preventDefault();
  }
}


// ------------------------- CREATE CIRCUITS BY PROYECTS, TGS AND TDS --------------------

// ----------- SELECT PROYECTS -----------------------

function proyect(element){
  console.log(element.value);
  $.ajax({
    url: "/api/tgs",
    method: 'POST',
    data: {proyect: element.value},
    success: (data, textStatus, xhr) => {
      console.log(data, textStatus, xhr);
      if (textStatus === 'success'){
        tableSelect = document.getElementById("tg-select");
        content = '<option selected>-Seleccione Tablero General-</option>';
        data.map(elmt => {
          content += `<option value=${elmt.id}>${elmt.name}</option>`
        });
        tableSelect.innerHTML = content;
        const h6Element = document.getElementById('td-h6');
        h6Element.style.display = 'none';
      
        const selectElement = document.getElementById("td-select");
        selectElement.style.display = 'none';  
      }
    },
    error: (xhr, textStatus, error) => {
      console.log(xhr, textStatus, error);
    },
  });
}

// ----------- SELECT TDS BY TGS -----------------------

function tds(element) {
  console.log(element.value);
  $.ajax({
    url: '/api/tds',
    method: 'POST',
    data: { tgs: element.value },
    success: (data, textStatus, xhr) => {
      console.log(data)
      if (Array.isArray(data[0]) && data[0].length > 0) {
        // Cambiar el estado de display del select
        const selectElement = document.getElementById("td-select");
        selectElement.style.display = 'block';
        const h6Element = document.getElementById('td-h6');
        h6Element.style.display = 'block';
        tableSelect = document.getElementById("td-select");
        content = '<option selected>-Seleccione Tablero de Distribución-</option>';
        data[0].map(xl => {
          content += `<option value=${xl.id}>${xl.name}</option>`
        });
        tableSelect.innerHTML = content;
      }
      else {
        // Código para cuando data está vacío
        const h6Element = document.getElementById('td-h6');
        h6Element.style.display = 'none';
      
        const selectElement = document.getElementById("td-select");
        selectElement.style.display = 'none';
      }
      },
      error: (xhr, textStatus, error) => {
        console.log(xhr, textStatus, error);
      },
    });
}
// ----------- VIEW LOADBOX PAGE -----------------------

// ----------- SELECT PROYECTS AND TGS -----------------------

function select_proyect(element){
  console.log(element.value);
  $.ajax({
    url: '/api/tgs',
    method: 'POST',
    data: {proyect: element.value},
    success: (data, textStatus, xhr) => {
      console.log(data)
      if (Array.isArray(data) && data.length > 0) {
        // Cambiar el estado de display del select
        const selectElement1 = document.getElementById("for-tgs");
        const selectElement2 = document.getElementById("h6-tgs");
        const selectElement6= document.getElementById("proyect-id");
        const selectElement7= document.getElementById("h6-pro");
        selectElement1.style.display = 'block';
        selectElement2.style.display = 'none';
        selectElement6.style.display = 'block';
        selectElement7.style.display = 'none';

        tableSelect = document.getElementById("tgs-id");
        content = '';
        data.map(xl => {
          content += `<option value=${xl.id}>${xl.name}</option>`
        });
        tableSelect.innerHTML = content;
        const divhide = document.getElementById('for-tds');
        const divshow = document.getElementById('h6-tds');
        divhide.style.display = 'none';
        divshow.style.display = 'block';
        const selectElement3 = document.getElementById("tg-circuit");
        const selectElement4 = document.getElementById("h6-circuit");
        const selectElement5 = document.getElementById("td-circuit");
        selectElement3.style.display = 'none';
        selectElement4.style.display = 'block';
        selectElement5.style.display = 'none';
        selectElement6.style.display = 'block';
        selectElement7.style.display = 'none';
      }
      else {
        // Código para cuando data está vacío
        const divhide1 = document.getElementById('for-tgs');
        const divhide2 = document.getElementById('h6-tgs');
        const divhide3 = document.getElementById('for-tds');
        const divshow4 = document.getElementById('h6-tds');
        const selectElement3 = document.getElementById("tg-circuit");
        const selectElement4 = document.getElementById("h6-circuit");
        const selectElement5 = document.getElementById("td-circuit");
        const selectElement6= document.getElementById("proyect-id");
        const selectElement7= document.getElementById("h6-pro");
        divhide1.style.display = 'none';
        divhide2.style.display = 'block';
        divhide3.style.display = 'none';
        divshow4.style.display = 'block';
        selectElement3.style.display = 'none';
        selectElement4.style.display = 'block';
        selectElement5.style.display = 'none';
        selectElement6.style.display = 'none';
        selectElement7.style.display = 'block';
      }
      },
      error: (xhr, textStatus, error) => {
        console.log(xhr, textStatus, error);
      },
    });
}

// ----------- SELECT TDS -----------------------


function select_tds(element) {
  console.log(element.value);
  $.ajax({
    url: '/api/tds',
    method: 'POST',
    data: { tgs: element.value},
    success: (data, textStatus, xhr) => {
      console.log(data);
      if (Array.isArray(data[0]) && data[0].length > 0) {
        // Cambiar el estado de display del select
        const selectElement1 = document.getElementById("for-tds");
        const selectElement2 = document.getElementById("h6-tds");
        selectElement2.style.display = 'none';
        selectElement1.style.display = 'block';
        tableSelect = document.getElementById("tds-id");
        content = '';
        data[0].map(xl => {
          content += `<option value=${xl.id}>${xl.name}</option>`;
        });
        tableSelect.innerHTML = content;
        if (Array.isArray(data[1]) && data[1].length > 0) {
          const selectElement1 = document.getElementById("tg-circuit");
          const selectElement2 = document.getElementById("h6-circuit");
          selectElement1.style.display = 'block';
          selectElement2.style.display = 'none';
        
          const tableCircuit = document.getElementById("tg-tbody-td");
          let content = '';
        
          data[1].forEach(xl => {
            content += `
              <tr class="border-top border-dark-subtle text-center">
                <td class="border-end border-dark-subtle">${xl.ref}</td>
                <td class="border-end border-dark-subtle">${xl.name}</td>
                <td class="border-end border-dark-subtle">${xl.power}</td>
                <td class="border-end border-dark-subtle">${xl.total_current}</td>
                <td class="border-end border-dark-subtle">220</td>
                <td><a href="#" class="me-2">Ver</a><a href="#" class="me-2">Editar</a><a href="#" class="me-2">Borrar</a></td>
              </tr>`;
          });
          
          tableCircuit.innerHTML = content;

        } else {
          const selectElement1 = document.getElementById("tg-circuit");
          const selectElement2 = document.getElementById("h6-circuit");
          selectElement1.style.display = 'none';
          selectElement2.style.display = 'block';
        }
        
      } else {
        // Código para cuando data está vacío
        const divhide = document.getElementById('for-tds');
        const divshow = document.getElementById('h6-tds');
        divhide.style.display = 'none';
        divshow.style.display = 'block';
      }
    },
    error: (xhr, textStatus, error) => {
      console.log(xhr, textStatus, error);
    },
  });
}

// // ----------- VIEW CIRCUITS -----------------------


var tgsSelect = document.getElementById("tgs-id");
var tdsSelect = document.getElementById("tds-id");

tgsSelect.addEventListener("change", obtenerValoresSeleccionados);
tdsSelect.addEventListener("change", obtenerValoresSeleccionados);

function obtenerValoresSeleccionados() {
  var tgsSelectedValues = getSelectedValues(tgsSelect);
  var tdsSelectedValues = getSelectedValues(tdsSelect);

  select_circuitTD(tgsSelectedValues, tdsSelectedValues);
}

function getSelectedValues(select) {
  var selectedValues = [];
  var options = select.options;

  for (var i = 0; i < options.length; i++) {
    if (options[i].selected) {
      selectedValues.push(options[i].value);
    }
  }

  return selectedValues;
}

function select_circuitTD(tgsSelectedValues, tdsSelectedValues) {
  console.log(tgsSelectedValues, tdsSelectedValues);
  $.ajax({
    url: '/api/circuits_td',
    method: 'POST',
    data: { tgs: tgsSelectedValues, tds: tdsSelectedValues },
    success: (data, textStatus, xhr) => {
      console.log(data);
      if (Array.isArray(data) && data.length > 0) {
        // Cambiar el estado de display del select
        const selectElement1 = document.getElementById("td-circuit");
        const selectElement2 = document.getElementById("h6-circuit");
        selectElement1.style.display = 'block';
        selectElement2.style.display = 'none';
        const tableCircuit = document.getElementById("td-tbody-td")
        content = '';
        data.map(xl => {
          content += 
          `<tr class="border-top border-dark-subtle text-center">
            <td class="border-end border-dark-subtle">${xl.ref}</td>
            <td class="border-end border-dark-subtle">${xl.name}</td>
            <td class="border-end border-dark-subtle">${xl.power}</td>
            <td class="border-end border-dark-subtle">${xl.total_current}</td>
            <td class="border-end border-dark-subtle">220</td>
            <td><a href="#" class="me-2">Ver</a><a href="#" class="me-2">Editar</a><a href="#" class="me-2">Borrar</a></td>
          </tr>`;
        });
        console.log(content);
        tableCircuit.innerHTML = content;
        console.log(tableCircuit);
      } else {
        // Código para cuando data está vacío
        const selectElement1 = document.getElementById("tg-circuit");
        const selectElement2 = document.getElementById("h6-circuit");
        selectElement1.style.display = 'none';
        selectElement2.style.display = 'block';
      }
    },
    error: (xhr, textStatus, error) => {
      console.log(xhr, textStatus, error);
    },
  });
}

