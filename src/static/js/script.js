// ---------------------------------------------------------------------------------------
// -------------------------CONFIRMACION CIERRE DE SESION---------------------------------

function confirmar(event) {
  if (!confirm('¿Estás seguro de que quieres cerrar sesión?')) {
    event.preventDefault();
  }
}

//  ------------------------ SUCCESS AL AGREGAR CIRCUITOS --------------------------------

function addCircuit(event){

}

// ------------------------- CREATE CIRCUITS BY PROYECTS, TGS AND TDS --------------------

// ------------------------------------------------- SELECT PROYECTS --------------------------------------------------

function proyect(element) {
  console.log(element.value);
  $.ajax({
    url: "/api/tgs",
    method: 'POST',
    data: { proyect: element.value },
    success: (data, textStatus, xhr) => {
      console.log(data, textStatus, xhr);
      const tableSelect = document.getElementById("tg-select");
      const tableSelect2 = document.getElementById("tg-select2");
      let content = '';

      if (textStatus === 'success' && data.length > 0) {

        const selectElement3 = document.getElementById("tg-h5");
        selectElement3.style.display = 'none';

      } else {
        const h6Element = document.getElementById('td-h6');
        h6Element.style.display = 'none';
      
        const selectElement = document.getElementById("td-select");
        selectElement.style.display = 'none';

      }

      content = '<option selected>-Seleccione Tablero General-</option>';
      if (data.length > 0) {
        data.map(elmt => {
          content += `<option value=${elmt.id}>${elmt.name}</option>`;
          const selectElement3 = document.getElementById("tg-h5");
          const selectElement4 = document.getElementById("div-tg");
          selectElement3.style.display = 'none';
          selectElement4.style.display = 'block';
        });
      } else {
        content = '<option selected>-No hay tableros generales-</option>';
        const selectElement3 = document.getElementById("tg-h5");
        const selectElement4 = document.getElementById("div-tg");
        selectElement3.style.display = 'block';
        selectElement4.style.display = 'none';
      }

      tableSelect.innerHTML = content;
      tableSelect2.innerHTML = content;
    },
    error: (xhr, textStatus, error) => {
      console.log(xhr, textStatus, error);
    }
  });
}




// ----------------------------------------------- SELECT TDS BY TGS ---------------------------------------------------

function tds(element) {
  console.log(element.value);
  $.ajax({
    url: '/api/tds',
    method: 'POST',
    data: { tgs: element.value },
    success: (data, textStatus, xhr) => {
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
        selectElement.innerHTML = '';
      }
    },
    error: (xhr, textStatus, error) => {
      console.log(xhr, textStatus, error);
    },
  });
}

// -------------------------------------------- VIEW LOADBOX PAGE -----------------------------------------------------

// ----------------------------------------- SELECT PROYECTS AND TGS --------------------------------------------------

function select_proyect(element){
  console.log(element.value);
  $.ajax({
    url: '/api/tgs',
    method: 'POST',
    data: {proyect: element.value},
    success: (data, textStatus, xhr) => {
      if (Array.isArray(data) && data.length > 0) {
        // Cambiar el estado de display del select
        const selectElement1 = document.getElementById("for-tgs");
        const selectElement2 = document.getElementById("h6-tgs");
        const selectElement3 = document.getElementById('for-tds');
        const selectElement4 = document.getElementById('h6-tds');
        const selectElement5 = document.getElementById("tg-circuit");
        const selectElement6 = document.getElementById("h6-circuit");
        const selectElement7 = document.getElementById("td-circuit");
        const selectElement8 = document.getElementById("h6-circuit2");
        const selectElement9 = document.getElementById("h5-circuit");        
        selectElement1.style.display = 'block';
        selectElement2.style.display = 'none';
        selectElement3.style.display = 'none';
        selectElement4.style.display = 'block';
        selectElement5.style.display = 'none';
        selectElement6.style.display = 'block';
        selectElement7.style.display = 'none';
        selectElement8.style.display = 'block';
        selectElement9.style.display = 'none';
        tableSelect = document.getElementById("tgs-id");
        content = '';
        data.map(xl => {
          content += `<option value=${xl.id}>${xl.name}</option>`
        });
        tableSelect.innerHTML = content;
      }
      else {
        // Código para cuando data está vacío
        const selectElement1 = document.getElementById("for-tgs");
        const selectElement2 = document.getElementById("h6-tgs");
        const selectElement3 = document.getElementById('for-tds');
        const selectElement4 = document.getElementById('h6-tds');
        const selectElement5 = document.getElementById("tg-circuit");
        const selectElement6 = document.getElementById("h6-circuit");
        const selectElement7 = document.getElementById("td-circuit");
        const selectElement8 = document.getElementById("h6-circuit2");
        const selectElement9 = document.getElementById("h5-circuit");        
        selectElement1.style.display = 'none';
        selectElement2.style.display = 'block';
        selectElement3.style.display = 'none';
        selectElement4.style.display = 'block';
        selectElement5.style.display = 'none';
        selectElement6.style.display = 'block';
        selectElement7.style.display = 'none';
        selectElement8.style.display = 'block';
        selectElement9.style.display = 'none';
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
      if (Array.isArray(data[0]) && data[0].length > 0) {
        // Cambiar el estado de display del select
        const selectElement1 = document.getElementById("h6-tds");
        const selectElement2 = document.getElementById("for-tds");
        selectElement1.style.display = 'none';
        selectElement2.style.display = 'block';        
        tableSelect = document.getElementById("tds-id");
        content = '';
        data[0].map(xl => {
          content += `<option value=${xl.id}>${xl.name}</option>`;
        });
        tableSelect.innerHTML = content;
      } else {
        const selectElement1 = document.getElementById("h6-tds");
        const selectElement2 = document.getElementById("for-tds");
        selectElement1.style.display = 'block';
        selectElement2.style.display = 'none';
        }

      if (Array.isArray(data[1]) && data[1].length > 0) {
        const selectElement1 = document.getElementById("h6-circuit");
        const selectElement2 = document.getElementById("h6-circuit2");
        const selectElement3 = document.getElementById("h5-circuit");
        const selectElement4 = document.getElementById("td-circuit");
        const selectElement5 = document.getElementById("tg-circuit");
        selectElement1.style.display = 'none';
        selectElement2.style.display = 'none';
        selectElement3.style.display = 'none';
        selectElement4.style.display = 'none';
        selectElement5.style.display = 'block';
        
        const tableCircuit = document.getElementById("tg-tbody-td");
        let content = '';
        let count = [];
      
        data[1].forEach(xl => {
          if (!count.includes(xl.circuit_id)){
          content += `
            <tr class="border-top border-dark-subtle text-center">
              <td class="border-end border-dark-subtle">${xl.ref}</td>
              <td class="border-end border-dark-subtle">${xl.name}</td>
              <td class="border-end border-dark-subtle">${xl.total_center}</td>
              <td class="border-end border-dark-subtle">${xl.total_current_ct}</td>
              <td class="border-end border-dark-subtle">${xl.total_power_ct}</td>
              <td><button type="button" class="btn btn-outline-secondary me-2 my-1 btn-sm" onclick="detail_circuit(this)" data-circuit-id="${xl.circuit_id}" data-bs-toggle="modal" data-bs-target="#staticBackdrop2">Ver</button><button class="btn btn-outline-secondary btn-sm my-1">Borrar</button></td>
            </tr>`;
            count.push(xl.circuit_id)
            }
          });

          tableCircuit.innerHTML = content;

      } else {
        const selectElement1 = document.getElementById("h6-circuit");
        const selectElement2 = document.getElementById("h6-circuit2");
        const selectElement3 = document.getElementById("h5-circuit");
        const selectElement4 = document.getElementById("td-circuit");
        const selectElement5 = document.getElementById("tg-circuit");
        selectElement1.style.display = 'block';
        selectElement2.style.display = 'none';
        selectElement3.style.display = 'block';
        selectElement4.style.display = 'none';
        selectElement5.style.display = 'none';
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
  $.ajax({
    url: '/api/circuits_td',
    method: 'POST',
    data: { tgs: tgsSelectedValues, tds: tdsSelectedValues },
    success: (data, textStatus, xhr) => {
      if (Array.isArray(data) && data.length > 0) {
        // Cambiar el estado de display del select
        console.log(data);
        const selectElement1 = document.getElementById("h6-circuit");
        const selectElement2 = document.getElementById("h6-circuit2");
        const selectElement3 = document.getElementById("h5-circuit");
        const selectElement4 = document.getElementById("td-circuit");
        const selectElement5 = document.getElementById("tg-circuit");
        selectElement1.style.display = 'none';
        selectElement2.style.display = 'none';
        selectElement3.style.display = 'none';
        selectElement4.style.display = 'block';
        selectElement5.style.display = 'none';

        const tableCircuit = document.getElementById("td-tbody-td");
        const addedNames = [];
        let content = '';
        
        data.forEach(xl => {
          if (!addedNames.includes(xl.circuit_id)) {
            content += 
              `<tr class="border-top border-dark-subtle text-center">
                <td class="border-end border-dark-subtle">${xl.ref}</td>
                <td class="border-end border-dark-subtle">${xl.name}</td>
                <td class="border-end border-dark-subtle">${xl.total_power}</td>
                <td class="border-end border-dark-subtle">${xl.total_current}</td>
                <td class="border-end border-dark-subtle">220</td>
                <td>
                  <button type="button" onclick="detail_circuit(this)" class="btn btn-sm btn-outline-secondary me-2 my-1" data-circuit-id="${xl.circuit_id}" data-bs-toggle="modal" data-bs-target="#staticBackdrop2">Ver</button>
                  <button class="btn btn-sm btn-outline-secondary my-1">Borrar</button>
                </td>
              </tr>`;
            addedNames.push(xl.circuit_id);
          }
        });
        
        tableCircuit.innerHTML = content;
        
      } else {
        // Código para cuando data está vacío
        const selectElement1 = document.getElementById("h6-circuit");
        const selectElement2 = document.getElementById("h6-circuit2");
        const selectElement3 = document.getElementById("h5-circuit");
        const selectElement4 = document.getElementById("td-circuit");
        const selectElement5 = document.getElementById("tg-circuit");
        selectElement1.style.display = 'block';
        selectElement2.style.display = 'none';
        selectElement3.style.display = 'block';
        selectElement4.style.display = 'none';
        selectElement5.style.display = 'none';
      }
    },
    error: (xhr, textStatus, error) => {
      console.log(xhr, textStatus, error);
    },
  });
}



function detail_circuit(element) {
  var circuitId = element.getAttribute("data-circuit-id");
  console.log(circuitId);
  $.ajax({
    url: `/api/detail`,
    method: "POST",
    data: { circuit: circuitId },
    success: (data, textStatus, xhr) => {
      console.log(data);
      if (textStatus === "success") {
        const nameCircuit = document.getElementById("nameCircuit")
        const detailTable = document.getElementById("detail-circuit-body");
        const detailLoad = document.getElementById("detail-circuit-loads-body");
        let html = '';
        
        if (data.length > 0) {
          const xl = data[0];
          console.log("circuitId:", circuitId);
          console.log("xl.id:", xl.id);
          html += 
            `<tr class="border border-dark-subtle text-center" style="font-size: 15px;">
              <td class="border border-dark-subtle">${xl.total_center}</td>
              <td class="border border-dark-subtle">${xl.total_power_ct}</td>
              <td class="border border-dark-subtle">${xl.total_current_ct}</td>`;
        
          if (xl.type_circuit === 'feeder') {
            html += `<td class="border border-dark-subtle">Alimentador</td>`;
          } else {
            html += `<td class="border border-dark-subtle">Subalimentador</td>`;
          }
        
          html += `
              <td class="border border-dark-subtle">${xl.largo}</td>
              <td class="border border-dark-subtle">${xl.fp}</td>
              <td class="border border-dark-subtle">${xl.vp}</td>
              <td class="border border-dark-subtle">${xl.wires}</td>
              <td class="border border-dark-subtle">${xl.secctionmm2}</td>
              <td class="border border-dark-subtle">${xl.breakers}</td>
              <td class="border border-dark-subtle">${xl.elect_differencial}</td>
              <td>
                <button type="button" class="btn btn-sm btn-outline-secondary my-1" onclick="addload(this)" data-circuit-id="${xl.circuit_id}" data-bs-toggle="modal" data-bs-target="#staticBackdrop3">Agregar Cargas</button>
              </td>
            </tr>`;
        }
        
        detailTable.innerHTML = html;        
            content = '';
            data.map(xl => {
              content += 
              `<tr class="border border-dark-subtle text-center">
                <td class="border border-dark-subtle">${xl.nameloads}</td>
                <td class="border border-dark-subtle">${xl.qty}</td>
                <td class="border border-dark-subtle">${xl.power}</td>
                <td class="border border-dark-subtle">${xl.total_power}</td>
                <td class="border border-dark-subtle">${xl.total_current}</td>
                <td>
                  <button type="button" class="btn btn-sm btn-outline-secondary my-1" data-circuit-id="${xl.circuit_id}" data-bs-toggle="modal" data-bs-target="#">Borrar</button>
                </td>
              </tr>`;
            });
        detailLoad.innerHTML = content;
        nameCircuit.innerHTML = "Circuito N° " + circuitId;
        const addLoad = document.getElementById("add");
        addLoad.innerHTML = 
        `<div class="input-group my-3">
          <span class="input-group-text" id="basic-addon1">Referencia</span>
          <input type="text" class="form-control" placeholder="Ubicación o referencia de la carga" aria-label="Username" aria-describedby="basic-addon1" name="nameloads">
        </div>
        <div class="input-group mt-3">
              <span class="input-group-text" id="basic-addon1">Cantidad de Cargas</span>
              <input type="number" class="form-control" placeholder="Ingresa la cantidad" aria-label="Username" aria-describedby="basic-addon1" name="qty">
              <input type="hidden" class="form-control" aria-label="Username" aria-describedby="basic-addon1" name="circuit_id" value=${data[0]['circuit_id']}>
        </div>
        <div class="input-group mt-3">
              <span class="input-group-text" id="basic-addon1">Potencia por Carga</span>
              <input type="text" class="form-control" placeholder="Ingresa la Potencia" aria-label="Username" aria-describedby="basic-addon1" name="power">
        </div>
        <div class="form-text" id="basic-addon4">La Potencia debe ser en Watt.</div>`;
      }
    }
  });
}


// function addload(element){
//   var dataEdit = element.getAttribute("data-circuit-id");
//   console.log(dataEdit);
//   $.ajax({
//     url:'/api/add_loads',
//     method: "POST",
//     data: {id_circuit: dataEdit},
//     success: (data, textStatus, xhr) => {
//       if (textStatus === 'success'){
//       console.log(data)
//       const addLoad = document.getElementById("add");
//     }
//       console.log(content);
//     }
//   });
// }

// function edit(element){
//   var dataAdd = element.getAttribute("data-add-circuit");
//   console.log(dataAdd);
//   $.ajax({
//     url:'/api/edit_circuit',
//     method: "POST",
//     data: {id_circuit: dataAdd},
//     success: (data, textStatus, xhr) => {
//       if (textStatus === 'success'){
//       console.log(data)
//       const editCircuit = document.getElementById("edit");
//       content = '';
//       data.forEach(edt => {
//         content +=
//         `
//         <div class="input-group mt-3">
//         <span class="input-group-text" id="basic-addon1">Cantidad de Cargas</span>
//           <input type="number" class="form-control" placeholder="Ingresa la cantidad total de cargas" aria-label="Username" aria-describedby="basic-addon1" name="qty">
//           <input type="hidden" class="form-control" placeholder="Ingresa la cantidad total de cargas" aria-label="Username" aria-describedby="basic-addon1" name="fp" value="1">
//         </div>
//         <div class="input-group mt-3">
//         <span class="input-group-text" id="basic-addon1">Potencia por Carga</span>
//         <input type="text" class="form-control" placeholder=${edt.power} aria-label="Username" aria-describedby="basic-addon1" name="power">
//         </div>
//         <div class="form-text" id="basic-addon4">La Potencia debe ser en Watt.</div>
//         <div class="input-group mt-3">
//         <span class="input-group-text" id="basic-addon1">Ingresa el Voltaje</span>
//         <select class="form-select" aria-label="Default select example" name="single_voltage">
//             <option selected>Selecciona un voltaje</option>
//             <option value="0.220">220</option>
//             <option value="0.380" disabled>380</option>
//         </select>
//         </div>
//         <div class="input-group mt-3">
//         <span class="input-group-text" id="basic-addon3">Largo del Circuito</span>
//         <input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3 basic-addon4" placeholder=${edt.largo} name="length">
//         </div>
//         <div class="form-text" id="basic-addon4">Ingresa el largo total del circuito en metros separado por punto.</div>`
//       });
//       console.log(content);
//       editCircuit.innerHTML = content;
//     }
//   }
//   })
// }