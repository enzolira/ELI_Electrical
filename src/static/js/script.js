// -----------------------------------------------------------------------------------------------------------------------------------
// -----------------------------------------------------------------------------------------------------------------------------------
// ------------------------------------CREATED OF PROYECT, TGS , TDS AND CIRCUITS-----------------------------------------------------
// -----------------------------------------------------------------------------------------------------------------------------------
// -----------------------------------------------------------------------------------------------------------------------------------

// -------------------------CONFIRMACION CIERRE DE SESION---------------------------------

function confirmar(event) {
  event.preventDefault();
  Swal.fire({
    icon:'question',
    title:'¿Estás seguro de que quieres cerrar sesión?',
    showConfirmButton:true,
    showCancelButton:true,
    confirmButtonColor: '#dc3545',
    cancelButtonColor: '#6c757d',
    cancelButtonText: 'Cancelar',
    confirmButtonText: 'Salir',
    width: '50%',
    position:'top'
  }).then((result) => {
    if (result.isConfirmed){
      window.location.href = event.target.href;
    }
  })
}

// ------------------------- CREATE CIRCUITS BY PROYECTS, TGS AND TDS --------------------


function addCircuit(){
const Toast = Swal.mixin({
  toast: true,
  position: 'top-end',
  showConfirmButton: false,
  timer: 3000,
  timerProgressBar: true,
  didOpen: (toast) => {
    toast.addEventListener('mouseenter', Swal.stopTimer)
    toast.addEventListener('mouseleave', Swal.resumeTimer)
  }
})

Toast.fire({
  icon: 'success',
  title: '¡Circuito agregado correctamente!'
})
}

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



// ----------------------------------------------- INPUT FACTOR DE POTENCIA ---------------------------------------------------

function factorPower(element) {
  const FpFactor = element.value;
  const factorID = document.getElementById('factorFP');
  if (FpFactor === "0.380") {
    factorID.style.display = 'block';
    console.log(FpFactor);
  }else{
    factorID.style.display = 'none';
  console.log(FpFactor);
  }
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
              <td class="border-end border-dark-subtle">${xl.total_power_ct}</td>
              <td class="border-end border-dark-subtle">${xl.total_current_ct}</td>`;
                if (xl.single_voltage === '0.220') {
                  content += `<td class="border-end border-dark-subtle">220</td>`;
                } else {
                  content += `<td class="border-end border-dark-subtle">380</td>`;
                }
                content += `
              <td><button type="button" class="btn btn-outline-secondary me-2 my-1 btn-sm" onclick="detail_circuit(this)" data-circuit-id="${xl.circuit_id}" data-bs-toggle="modal" data-bs-target="#staticBackdrop2">Ver</button><button class="btn btn-sm btn-outline-danger my-1" data_circuit_delete2="${xl.circuit_id}" onclick="deleteCircuit(this)">Borrar</button></td>
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

if (tgsSelect && tdsSelect) {
  tgsSelect.addEventListener("change", obtenerValoresSeleccionados);
  tdsSelect.addEventListener("change", obtenerValoresSeleccionados);
}

// tgsSelect.addEventListener("change", obtenerValoresSeleccionados);
// tdsSelect.addEventListener("change", obtenerValoresSeleccionados);

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
                <td class="border-end border-dark-subtle">${xl.total_power_ct}</td>
                <td class="border-end border-dark-subtle">${xl.total_current_ct}</td>`;
                if (xl.single_voltage === '0.220') {
                  content += `<td class="border-end border-dark-subtle">220</td>`;
                } else {
                  content += `<td class="border-end border-dark-subtle">380</td>`;
                }
                content += `
                <td>
                  <button type="button" onclick="detail_circuit(this)" class="btn btn-sm btn-outline-secondary me-2 my-1" data-circuit-id="${xl.circuit_id}" data-bs-toggle="modal" data-bs-target="#staticBackdrop2">Ver</button>
                  <button class="btn btn-sm btn-outline-danger my-1" data_circuit_delete2="${xl.circuit_id}" onclick="deleteCircuit(this)">Borrar</button>
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
            `<tr class="border border-dark-subtle text-center" style="font-size: 15px; height: 40px;">
              <td>${xl.total_center}</td>
              <td>${xl.total_power_ct}</td>
              <td>${xl.total_current_ct}</td>`;
      
              if (xl.fp === '1.00') {
                html += `<td>1</td>`;
              } else {
                html += `<td>${xl.fp}</td>`;
              }
        
              if (xl.single_voltage === '0.220') {
                html += `<td>220</td>`;
              } else {
                html += `<td>380</td>`;
              }
          html += `
              <td>${xl.total_length_ct}</td>
              <td>${xl.vp}</td>
              <td>${xl.wires}</td>
              <td>${xl.secctionmm2}</td>
              <td>${xl.breakers}</td>
              <td>${xl.elect_differencial}</td>
            </tr>`;
        }
        
        detailTable.innerHTML = html;     
            content = '';
            data.map(xl => {
              content += 
              `<tr class="border border-dark-subtle text-center">
                <td class="border border-dark-subtle">${xl.nameloads}</td>
                <td class="border border-dark-subtle">${xl.largo}</td>
                <td class="border border-dark-subtle">${xl.qty}</td>
                <td class="border border-dark-subtle">${xl.power}</td>
                <td class="border border-dark-subtle">${xl.total_power}</td>
                <td class="border border-dark-subtle">${xl.total_current}</td>
                <td class="border border-dark-subtle"><button class="btn btn-sm btn-outline-danger my-1" data_circuit=${xl.circuit_id} data_circuit_delete=${xl.id} onclick="deleteLoad(this)">Borrar</button></td>
              </tr>`;
            });
        detailLoad.innerHTML = content;
        nameCircuit.innerHTML = "<strong>Cuadro de Resumén Circuito N° " + data[0]['name'] + "</strong>";
        const addLoad = document.getElementById("add");
        if (data[0]['single_voltage'] === '0.220'){
        addLoad.innerHTML = 
        `<div class="input-group my-3">
          <span class="input-group-text" id="basic-addon1">Referencia</span>
          <input type="text" class="form-control" placeholder="Ubicación o referencia de la carga" aria-label="Username" aria-describedby="basic-addon1" name="nameloads">
        </div>
        <div class="input-group mt-3">
              <span class="input-group-text" id="basic-addon1">Cantidad de Cargas</span>
              <input type="number" class="form-control" placeholder="Ingresa la cantidad" aria-label="Username" aria-describedby="basic-addon1" name="qty">
              <input type="hidden" class="form-control" aria-label="Username" aria-describedby="basic-addon1" name="circuit_id" value=${data[0]['circuit_id']}>
              <input type="hidden" class="form-control" aria-label="Username" aria-describedby="basic-addon1" name="fp" value=${data[0]['fp']}>
        </div>
        <div class="input-group mt-3">
              <span class="input-group-text" id="basic-addon1">Potencia por Carga</span>
              <input type="text" class="form-control" placeholder="Ingresa la Potencia" aria-label="Username" aria-describedby="basic-addon1" name="power">
        </div>
        <div class="form-text" id="basic-addon4">La Potencia debe ser en Watt.</div>
        <div class="input-group mt-2">
          <span class="input-group-text" id="basic-addon3">Distancia de la Carga</span>
          <input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3 basic-addon4" placeholder="Ejemplo: 12.5" name="total_length_ct">
        </div>
        <div class="form-text" id="basic-addon4">Ingresa el largo total del circuito en metros separado por punto.</div>`;

      } else {
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
          <span class="input-group-text" id="basic-addon1">Voltaje Definido</span>
          <select class="form-select" aria-label="Default select example" name="single_voltage">
            <option value="0.380" readonly>380V</option>
          </select>
        </div>
        <div id="factorFP2">
          <div class="input-group mt-3">
              <span class="input-group-text">Factor de Potencia</span>
              <input type="text" class="form-control" placeholder="Ingresa el Factor de Potencia" name="fp">
          </div>
          <div class="form-text" id="basic-addon4">Ingresa el Factor de Potencia separado por punto.</div>
        </div>
        <div class="input-group mt-3">
              <span class="input-group-text" id="basic-addon1">Potencia por Carga</span>
              <input type="text" class="form-control" placeholder="Ingresa la Potencia" aria-label="Username" aria-describedby="basic-addon1" name="power">
        </div>
        <div class="form-text" id="basic-addon4">La Potencia debe ser en Watt.</div>
        <div class="input-group mt-2">
          <span class="input-group-text" id="basic-addon3">Distancia de la Carga</span>
          <input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3 basic-addon4" placeholder="Ejemplo: 12.5" name="total_length_ct">
        </div>
        <div class="form-text" id="basic-addon4">Ingresa el largo total del circuito en metros separado por punto.</div>`;
      }
    }
    }
  });
}


// # --------------------- EDIT AND DELETE CIRCUITS BY TDS AND TGS -----------------------------------------------------------
// # --------------------- DELETE LOADS -----------------------------------------------------------

  
function deleteLoad(element) {
  const load_id = element.getAttribute("data_circuit_delete");
  const circuit_id1 = element.getAttribute("data_circuit");
  console.log(load_id)
  console.log(circuit_id1)
  Swal.fire({
    title: '¿Seguro que quieres Borrar esta Carga?',
    icon: 'warning',
    width: '50%',
    showCancelButton: true,
    confirmButtonColor: '#0d6efd',
    cancelButtonColor: '#6c757d',
    cancelButtonText: 'Cancelar',
    confirmButtonText: 'Sí, Borrar',
    allowOutsideClick: false,
    allowEnterKey: true,
    stopKeydownPropagation: false,
    position: 'top'
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire({
        title: 'Carga Borrada Correctamente',
        icon: 'success',
        allowOutsideClick: false,
        timer: 3000,
        position: 'top'
      });
      
      $.ajax({
        url:'/api/delete/load',
        method:'POST',
        data:{load: load_id , circuit:circuit_id1},
        success: (data, textStatus, xhr) => {
          var modal = document.getElementById("staticBackdrop2");
          var modalInstance = bootstrap.Modal.getInstance(modal);
          modalInstance.hide();
          var circuitId2 = element.getAttribute("data-circuit-id");
          detail_circuit(circuitId2);
        }
      })
    }
  });
}

// # --------------------- DELETE CIRCUIT -----------------------------------------------------------

function deleteCircuit(element) {
  const circuit_id2 = element.getAttribute("data_circuit_delete2");
  console.log(circuit_id2)
  Swal.fire({
    title: '¿Estás seguro de que deseas borrar el circuito?',
    text: 'Si hay cargas asociadas, ¡también se eliminarán!',
    icon: 'warning',
    width: '60%' ,
    showCancelButton: true,
    confirmButtonColor: '#0d6efd',
    cancelButtonColor: '#6c757d',
    cancelButtonText: 'Cancelar',
    confirmButtonText: 'Borrar',
    allowOutsideClick: false,
    allowEnterKey: true,
    stopKeydownPropagation: false,
    position: 'top'
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire({
        title: 'Circuito Borrado Correctamente',
        icon: 'success',
        allowOutsideClick: false,
        position: 'top'
      });
      
      $.ajax({
        url:'/api/delete/circuit',
        method:'POST',
        data:{ circuitv2: circuit_id2},
        success: (data, textStatus, xhr) => {
          location.reload();
        }
      })
    }
  });
}


// -----------------------------------------------------------------------------------------------------------------------------------
// -----------------------------------------------------------------------------------------------------------------------------------
// ----------------------------------------   SUMMARY PROYECT ------------------------------------------------------------------------
// -----------------------------------------------------------------------------------------------------------------------------------
// -----------------------------------------------------------------------------------------------------------------------------------

// function infoProyect(userId) {
//   $.ajax({
//     url: '/projects/details/',
//     method: 'GET',
//     data: { user_id: userId },
//     success: (data, textStatus, xhr) => {
//       const project = document.getElementById('id-projects');
//       let content = '';
//       let count = [];
//       let counter = 1;
//       data.forEach(pr => {
//         if (!count.includes(pr.name) && data.length !== 0) {
//           const targetId = counter;
//           content +=
//             `<button class="btn" data-bs-toggle="collapse" data-bs-target="#project${targetId}" style="width: 100%;" data-pro-id="${pr.id}" onclick="tg_circuit(this)">${pr.name}</button>
//             <div class="collapse" style="width: 100%;" id="project${targetId}">
//                 <div class="card card-body">
//                 </div>
//             </div>`;
//           count.push(pr.name);
//           counter++;
//         }
//       });
      
//       project.innerHTML = content;
//     },
//     error: (xhr, textStatus, error) => {
//       console.log(xhr, textStatus, error);
//     }
//   });
// }


//   document.addEventListener("DOMContentLoaded", function() {
//     const mainElement = document.getElementById("main");
//     if (mainElement && window.location.pathname === "/summary") {
//       const userId = mainElement.getAttribute("data-user-id");
//       infoProyect(userId);
//     }
//   });


  // function tg_circuit(element) {
  //   const proId = element.getAttribute('data-pro-id');
  //   const targetId = element.getAttribute('data-bs-target').substring(1);
    
  //   console.log(proId);
    
  //   $.ajax({
  //     url: '/api/pro_id/',
  //     method: 'GET',
  //     data: { proyect_id: proId },
  //     success: (data, textStatus, xhr) => {
  //       const targetTg = document.getElementById(targetId);
  //       let content = '';
        
  //       if (data.length !== 0) {
  //         data.forEach(tt => {
  //           content += `<h5>${tt.name}</h5>`;
  //           console.log(data)
  //         });
  //       }else {
  //         content += `<h5>Proyecto Vacio</h5>`;
  //         console.log(data)
  //       }
        
  //       targetTg.innerHTML = content;        
  //     },
  //     error: (xhr, textStatus, error) => {
  //       console.log(xhr, textStatus, error);
  //     }
  //   });
  // }


  function tg_circuit(element) {
    const dataBsTarget = element.dataset.bsTarget.substring(1);
    const tgId = document.getElementById(dataBsTarget);
    const dataProId = element.dataset.proId;
  
    console.log("data-bs-target:", dataBsTarget);
    console.log("data-pro-id:", dataProId);
  
    $.ajax({
      url: '/api/pro_id/',
      method: 'GET',
      data: { proyect_id: dataProId },
      success: (data, textStatus, xhr) => {
        let content = '';
        let count = 0;
        if (data.length !== 0) {
          data.forEach((tt) => {
            content += `
              <div class="card card-body">
                <h6>${tt.name}</h6>
                <div id="td${tt.id}" data-tg-circuit="${tt.id}" onclick='funcionJavaPrueba()></div>
              </div>`;
          
            td_circuit(tt.id, "td" + tt.id);
          });
          
        } else {
          content += 
          `<div class="card card-body">
            <h6>Proyecto Vacio</h6>
          </div>`;
        }        
        tgId.innerHTML = content;
      },
      error: (xhr, textStatus, error) => {
        console.log(xhr, textStatus, error);
      }
    });
  }
  

  function td_circuit(dataTgCircuit, id) {
    $.ajax({
      url:'/api/tg_id',
      method:'GET',
      data: { tg_id: dataTgCircuit },
      success: (data, textStatus, xhr) => {
        console.log(data)
        const divTd = document.getElementById(id);
        divTd.innerText = 'Probando'
      },
      error: ( xhr, textStatus, error) => {
        console.log(xhr, textStatus, error);
      }
    })
    
  }
  
  
  