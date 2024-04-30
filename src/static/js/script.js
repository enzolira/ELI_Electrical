// ------------------------------------------------------------------------------------------------
// ------------------------------------------------------------------------------------------------
// ------------------------------------CREATED OF PROYECT, TGS , TDS, CIRCUITS & LOADS-------------
// ------------------------------------------------------------------------------------------------
// ------------------------------------------------------------------------------------------------

// -------------------------CONFIRMACION CIERRE DE SESION---------------------------------

function confirmar(event) {
  event.preventDefault();
  Swal.fire({
    icon:'question',
    title:'¿Estás seguro de cerrar sesión?',
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

// ------------------------- CIERRE DE SESION DESPUES DE 15 MINUTOS DE INACTIVIDAD ---------------------------------

// let inactivityTimer;cer
// function iniciarTemporizador() {
//   clearTimeout(inactivityTimer);
//   inactivityTimer = setTimeout(function() {
//     cerrarSesion()
//   }, 15 * 60 * 1000);
// }

// function cerrarSesion() {
//   $.ajax({
//     url: "/logout",
//     method: 'GET',
//     success: () => {
//       location.reload();
//     },error: function() {
//     }
//   });
// }

// document.addEventListener("mousemove", iniciarTemporizador);
// document.addEventListener("keydown", iniciarTemporizador);

// ------------------------- CREATE CIRCUITS BY PROYECTS, TGS AND TDS --------------------

function addCircuit() {
  Swal.fire({
    position: 'top',
    icon: "success",
    title: '¡Circuito agregado correctamente!',
    showConfirmButton: false,
    timer: 2000,
    width: '35em'
  })
}

// ------------------------------------------------- SELECT PROYECTS --------------------------------------------------

function proyect(element) {
  $.ajax({
    url: "/api/tgs",
    method: 'POST',
    data: { proyect: element.value },
    success: (data, textStatus, xhr) => {
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

      content = '<option selected>-Seleccione tablero general-</option>';
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
        const tableSelect = document.getElementById("td-select");
        content = '<option selected>-Seleccione tablero de distribución-</option>';
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
  const voltageSelect = document.querySelector('select[name="single_voltage"]');
  const fpInput = document.querySelector('input[name="fp"]');
  const selectedVoltage = voltageSelect.value;
  if (FpFactor === "capacitance" && selectedVoltage === "0.220") {
    fpInput.value = "0.95";
    fpInput.disabled = true;
  } else if (FpFactor === "inductance" && selectedVoltage === "0.220") {
    fpInput.value = "0.93";
    fpInput.disabled = true;
  }
  else {
    fpInput.value = "";
    fpInput.disabled = false;
  }
}

function factorPower2(element) {
  const FpFactor2 = element.value;
  const fpInput2 = document.querySelector('input[name="fp2"]');
  if (FpFactor2 === "capacitance") {
      fpInput2.value = "0.95";
      fpInput2.disabled = true;
  } else if (FpFactor2 === "inductance") {
    fpInput2.value = "0.93";
    fpInput2.disabled = true;
  } 
}

function factorPower3(element) {
  const FpFactor3 = element.value;
  const voltageSelect3 = document.querySelector('select[name="voltage2"]');
  const fpInput = document.querySelector('input[name="fp3"]');
  const selectedVoltage3 = voltageSelect3.value;
  if (FpFactor3 === "capacitance" && selectedVoltage3 === "0.220") {
    fpInput.value = "0.95";
    fpInput.disabled = true;
  } else if (FpFactor3 === "inductance" && selectedVoltage3 === "0.220") {
    fpInput.value = "0.93";
    fpInput.disabled = true;
  } else if (selectedVoltage3 === "0.380"){
    fpInput.value = "";
    fpInput.disabled = false;
  }
}

// -------------------------------------------- VIEW LOADBOX PAGE -----------------------------------------------------

// ----------------------------------------- SELECT PROYECTS AND TGS --------------------------------------------------

function select_proyect(element){
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
        const selectElement10 = document.getElementById("buttons");             
        const selectElement11 = document.getElementById("buttons_tds");             
        selectElement1.style.display = 'block';
        selectElement2.style.display = 'none';
        selectElement3.style.display = 'none';
        selectElement4.style.display = 'block';
        selectElement5.style.display = 'none';
        selectElement6.style.display = 'block';
        selectElement7.style.display = 'none';
        selectElement8.style.display = 'block';
        selectElement9.style.display = 'none';
        selectElement10.style.display = 'block';
        selectElement11.style.display = 'none';
        tableSelect = document.getElementById("tgs-id");
        content = '';
        data.map(xl => {
          content += `<option value=${xl.id}>${xl.name}</option>`
        });
        tableSelect.innerHTML = content;
      }
      else {
        // Para cuando data está vacío
        const selectElement1 = document.getElementById("for-tgs");
        const selectElement2 = document.getElementById("h6-tgs");
        const selectElement3 = document.getElementById('for-tds');
        const selectElement4 = document.getElementById('h6-tds');
        const selectElement5 = document.getElementById("tg-circuit");
        const selectElement6 = document.getElementById("h6-circuit");
        const selectElement7 = document.getElementById("td-circuit");
        const selectElement8 = document.getElementById("h6-circuit2");
        const selectElement9 = document.getElementById("h5-circuit");              
        const selectElement10 = document.getElementById("buttons");  
        const selectElement11 = document.getElementById("buttons_tds");             
        selectElement1.style.display = 'none';
        selectElement2.style.display = 'block';
        selectElement3.style.display = 'none';
        selectElement4.style.display = 'block';
        selectElement5.style.display = 'none';
        selectElement6.style.display = 'block';
        selectElement7.style.display = 'none';
        selectElement8.style.display = 'block';
        selectElement9.style.display = 'none';
        selectElement10.style.display = 'none';
        selectElement11.style.display = 'none';
      }
      },
      error: (xhr, textStatus, error) => {
        console.log(xhr, textStatus, error);
      },
    });
}

// ----------- SELECT TDS -----------------------


function select_tds(element) {
  $.ajax({
    url: '/api/tds',
    method: 'POST',
    data: { tgs: element.value},
    success: (data, textStatus, xhr) => {
      if (Array.isArray(data[0]) && data[0].length > 0) {
        const selectElement1 = document.getElementById("h6-tds");
        const selectElement2 = document.getElementById("for-tds");
        const selectElement3 = document.getElementById("buttons");
        const selectElement4 = document.getElementById("buttons_tds");
        selectElement1.style.display = 'none';
        selectElement2.style.display = 'block';
        selectElement3.style.display = 'block';
        selectElement4.style.display = 'block';
        tableSelect = document.getElementById("tds-id");
        content = '';
        data[0].map(xl => {
          content += `<option value=${xl.id}>${xl.name}</option>`;
        });
        tableSelect.innerHTML = content;
      } else {
        const selectElement1 = document.getElementById("h6-tds");
        const selectElement2 = document.getElementById("for-tds");
        const selectElement3 = document.getElementById("buttons_tds");
        selectElement1.style.display = 'block';
        selectElement2.style.display = 'none';
        selectElement3.style.display = 'none';
        }

        if ((Array.isArray(data[2]) && data[2].length > 0) || (Array.isArray(data[1]) && data[1].length > 0)) {
        const selectElement1 = document.getElementById("h6-circuit");
        const selectElement2 = document.getElementById("h6-circuit2");
        const selectElement3 = document.getElementById("h5-circuit");
        const selectElement4 = document.getElementById("td-circuit");
        const selectElement5 = document.getElementById("tg-circuit");
        const selectElement6 = document.getElementById("buttons");
        selectElement1.style.display = 'none';
        selectElement2.style.display = 'none';
        selectElement3.style.display = 'none';
        selectElement4.style.display = 'none';
        selectElement5.style.display = 'block';
        selectElement6.style.display = 'block';
        
        const tableCircuit = document.getElementById("tg-tbody-td");
        let content = '';
        let count = [];
      
        if ((Array.isArray(data[2]) && data[2].length > 0) || (Array.isArray(data[1]) && data[1].length > 0)) {
          data[2].forEach(xl1 => {
              if (count.includes(xl1.circuit_id)){
                  content += `
                      <tr class="border-top border-dark-subtle text-center">
                          <td class="border-end border-dark-subtle">${xl1.ref}</td>
                          <td class="border-end border-dark-subtle">${xl1.name}</td>
                          <td class="border-end border-dark-subtle">${xl1.total_center}</td>
                          <td class="border-end border-dark-subtle">${xl1.total_active_power_ct}</td>
                          <td class="border-end border-dark-subtle">${xl1.total_current_ct}</td>`;
                  if (xl1.single_voltage === '0.220') {
                      content += `<td class="border-end border-dark-subtle">220</td>`;
                  } else {
                      content += `<td class="border-end border-dark-subtle">380</td>`;
                  }
                  content += `
                          <td class="border-bottom border-dark-subtle"><button type="button" class="btn btn-outline-secondary me-2 my-1 btn-sm" onclick="detail_circuit(this)" data-circuit-id="${xl1.circuit_id}" data-bs-toggle="modal" data-bs-target="#staticBackdrop2">Ver</button><button class="btn btn-sm btn-outline-danger my-1" data_circuit_delete2="${xl1.circuit_id}" onclick="deleteCircuit(this)">Borrar</button></td>
                      </tr>`;
                  count.push(xl1.circuit_id)
              }
          });
      
          data[1].forEach(xl1 => {
              if (!count.includes(xl1.circuit_id)){
                  content += `
                      <tr class="border-top border-dark-subtle text-center">
                          <td class="border-end border-dark-subtle">${xl1.ref}</td>
                          <td class="border-end border-dark-subtle">${xl1.name}</td>
                          <td class="border-end border-dark-subtle">${xl1.total_center}</td>
                          <td class="border-end border-dark-subtle">${xl1.total_active_power_ct}</td>
                          <td class="border-end border-dark-subtle">${xl1.total_current_ct}</td>`;
                  if (xl1.single_voltage === '0.220') {
                      content += `<td class="border-end border-dark-subtle">220</td>`;
                  } else {
                      content += `<td class="border-end border-dark-subtle">380</td>`;
                  }
                  content += `
                          <td><button type="button" class="btn btn-outline-secondary me-2 my-1 btn-sm" onclick="detail_circuit(this)" data-circuit-id="${xl1.circuit_id}" data-bs-toggle="modal" data-bs-target="#staticBackdrop2">Ver</button><button class="btn btn-sm btn-outline-danger my-1" data_circuit_delete2="${xl1.circuit_id}" onclick="deleteCircuit(this)">Borrar</button></td>
                      </tr>`;
                  count.push(xl1.circuit_id)
              }
          });
      }
      

        let sortedItemsNotEmpty = [];
        let sortedItemsEmpty = [];
        
        data[2].forEach(xl2 => {
            xl2.forEach(item => {
                if (item.total_center !== null) {
                    sortedItemsNotEmpty.push(item);
                } else {
                    sortedItemsEmpty.push(item);
                }
            });
        });
        
        // Concatenar los dos arreglos en el orden deseado
        let sortedItems = sortedItemsNotEmpty.concat(sortedItemsEmpty);
      

        //aca agregar el contenido ordenado segun si hay circuitos o no en el td
        sortedItems.forEach(item => {
            if (item.total_center === null) {
                content += `
                    <tr class="border-top border-dark-subtle text-center" style="height: 40px">
                        <td class="border-end border-dark-subtle">${item.ref}</td>
                        <td class="border-end border-dark-subtle">${item.name}</td>
                        <td class="pt-2" colspan="5"><h6>Sin circuitos</h6></td>
                        <td class="border-dark-subtle" style="height: 40px"></td>
                    </tr>`;
            } else {
                content += `
                    <tr class="border-top border-dark-subtle text-center" style="height: 40px">
                        <td class="border-end border-dark-subtle">${item.ref}</td>
                        <td class="border-end border-dark-subtle">${item.name}</td>
                        <td class="border-end border-dark-subtle">${item.total_center}</td>
                        <td class="border-end border-dark-subtle">${item.total_active_power_ct}</td>
                        <td class="border-end border-dark-subtle">${item.total_current_ct}</td>`;
                if (item.single_voltage === '0.220') {
                    content += `<td class="border-end border-dark-subtle">220</td>`;
                } else {
                    content += `<td class="border-end border-dark-subtle">380</td>`;
                }
                content += `
                    <td class="border-dark-subtle" style="height: 40px">
                      <button type="button" onclick="detail_tds(this)" class="btn btn-sm btn-outline-secondary me-2 my-1" style="width: 30%" data-td-id ="${item.td_id}" data-bs-toggle="modal" data-bs-target="#staticBackdrop4">Ver</button>
                    </td>
                </tr>`;
                count.push(item.circuit_id);
            }
        });

        // Mostrar el contenido en la tabla
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


let tgsSelect = document.getElementById("tgs-id");
let tdsSelect = document.getElementById("tds-id");

if (tgsSelect && tdsSelect) {
  tgsSelect.addEventListener("change", obtenerValoresSeleccionados);
  tdsSelect.addEventListener("change", obtenerValoresSeleccionados);
}


function obtenerValoresSeleccionados() {
  let tgsSelectedValues = getSelectedValues(tgsSelect);
  let tdsSelectedValues = getSelectedValues(tdsSelect);

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
        
        data.forEach((xl) => {
            if (!addedNames.includes(xl.circuit_id)) {
              content += 
                `<tr class="border-top border-dark-subtle text-center">
                  <td class="border-end border-dark-subtle">${xl.nameloads}</td>
                  <td class="border-end border-dark-subtle">${xl.name}</td>
                  <td class="border-end border-dark-subtle">${xl.total_center}</td>
                  <td class="border-end border-dark-subtle">${xl.total_active_power_ct}</td>
                  <td class="border-end border-dark-subtle">${xl.total_current_ct}</td>`;
                  if (xl.single_voltage === '0.220') {
                    content += `<td class="border-end border-dark-subtle">220</td>`;
                  } else {
                    content += `<td class="border-end border-dark-subtle">380</td>`;
                  }
                  content += `
                  <td class="">
                    <button type="button" onclick="detail_circuit(this)" class="btn btn-sm btn-outline-secondary me-2 my-1" data-circuit-id="${xl.circuit_id}" data-bs-toggle="modal" data-bs-target="#staticBackdrop2">Ver</button>
                    <button class="btn btn-sm btn-outline-danger my-1" data_circuit_delete2="${xl.circuit_id}" onclick="deleteCircuit(this)">Borrar</button>
                  </td>
                </tr>`;
              addedNames.push(xl.circuit_id);
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


function detail_circuit(element) {
  var circuitId = element.getAttribute("data-circuit-id");
  $.ajax({
    url: `/api/detail`,
    method: "POST",
    data: { circuit: circuitId },
    success: (data, textStatus, xhr) => {
      if (textStatus === "success") {
        const nameCircuit = document.getElementById("nameCircuit")
        const detailTable = document.getElementById("detail-circuit-body");
        const detailLoad = document.getElementById("detail-circuit-loads-body");
        let html = '';
        
        if (data.length > 0) {
          const xl = data[0];
          html += 
            `<tr class="border border-dark-subtle text-center" style="font-size: 15px; height: 40px;">
              <td>${xl.total_center}</td>
              <td>${xl.total_active_power_ct}</td>
              <td>${xl.total_current_ct}</td>`;

              if (xl.single_voltage === '0.220') {
                html += `<td>220</td>`;
              } else {
                html += `<td>380</td>`;
              }
              html += `<td>${xl.total_fp}</td>`;
              
              if (xl.name_impedance == "capacitance"){
                html += `<td>Capacitiva</td>`;
              } else {
                html += `<td>Inductiva</td>`;
              }

          html +=`    
              <td>${xl.total_length_ct}</td>
              <td>${xl.vp}</td>
              <td>${xl.method.toUpperCase()}</td>
              <td>${xl.wires}</td>
              <td>${xl.secctionmm2}</td>
              <td>${xl.conduit}</td>
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
                <td class="border border-dark-subtle">${parseInt(xl.active_power)}</td>
                <td class="border border-dark-subtle">${xl.total_active_power}</td>
                <td class="border border-dark-subtle">${xl.total_current}</td>`;
                if (xl.voltage === '0.220') {
                  content += `<td class="border border-dark-subtle">220</td>`;
                } else {
                  content += `<td class="border border-dark-subtle">380</td>`;
                  }
                  content += `<td class="border border-dark-subtle"><button class="btn btn-sm btn-outline-danger my-1" data_circuit=${xl.circuit_id} data_circuit_delete=${xl.id} onclick="deleteLoad(this)">Borrar</button></td></tr>`;
            });
        detailLoad.innerHTML = content;
        nameCircuit.innerHTML = "<strong>Cuadro de Resumén Circuito N° " + data[0]['name'] + "</strong>";
        const addLoad = document.getElementById("add");
        if (data[0]['single_voltage'] === '0.220'){
        addLoad.innerHTML = 
        `<div class="input-group my-3">
          <span class="input-group-text" id="basic-addon1">Nombre de la Carga</span>
          <input type="text" class="form-control" placeholder="Ingresa el nombre del consumo." aria-label="Username" aria-describedby="basic-addon1" name="nameloads">
        </div>
        <div class="input-group mt-3">
              <span class="input-group-text" id="basic-addon1">Cantidad de Cargas</span>
              <input type="number" class="form-control" placeholder="Ingresa la cantidad" aria-label="Username" aria-describedby="basic-addon1" name="qty">
              <input type="hidden" class="form-control" aria-label="Username" aria-describedby="basic-addon1" name="circuit_id" value=${data[0]['circuit_id']}>
        </div>
        <div class="input-group mt-3">
          <span class="input-group-text" id="basic-addon1">Voltaje</span>
          <select class="form-select" aria-label="Default select example" name="voltage">
            <option value="0.220" readonly>220</option>
          </select>
      </div>
      <div class="input-group mt-3">
          <span class="input-group-text" id="basic-addon1">Tipo de Impedancia</span>
          <select class="form-select" name="impedance" id="cap_ind" onchange="factorPower2(this)">
            <option selected>Selecciona un tipo</option>
            <option value="capacitance">Capacitiva</option>
            <option value="inductance">Inductiva</option>
          </select>
        </div>
        <div id="factorFP2">
          <div class="input-group mt-3">
            <span class="input-group-text">Factor de Potencia</span>
            <input type="text" class="form-control" placeholder="Ingresa el factor de potencia" name="fp2">
          </div>
          <div class="form-text ps-2" id="basic-addon4">Ingresa el factor de potencia separado por punto.</div>
        </div>
        <div class="input-group mt-2">
              <span class="input-group-text" id="basic-addon1">Potencia por Carga</span>
              <input type="text" class="form-control" placeholder="Ingresa la potencia" aria-label="Username" aria-describedby="basic-addon1" name="power">
        </div>
        <div class="form-text ps-2" id="basic-addon4">La potencia debe ser en watt.</div>
        <div class="input-group mt-2">
          <span class="input-group-text" id="basic-addon3">Distancia de la Carga</span>
          <input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3 basic-addon4" placeholder="Ejemplo: 12.5" name="total_length_ct">
        </div>
        <div class="form-text ps-2" id="basic-addon4">Ingresa el largo total del circuito en metros separado por punto.</div>`;

      } else {
        addLoad.innerHTML = 
        `<div class="input-group my-3">
          <span class="input-group-text" id="basic-addon1">Nombre de la Carga</span>
          <input type="text" class="form-control" placeholder="Ingresa el nombre del consumo." aria-label="Username" aria-describedby="basic-addon1" name="nameloads">
        </div>
        <div class="input-group mt-3">
              <span class="input-group-text" id="basic-addon1">Cantidad de Cargas</span>
              <input type="number" class="form-control" placeholder="Ingresa la cantidad" aria-label="Username" aria-describedby="basic-addon1" name="qty">
              <input type="hidden" class="form-control" aria-label="Username" aria-describedby="basic-addon1" name="circuit_id" value=${data[0]['circuit_id']}>
        </div>
        <div class="input-group mt-3">
          <span class="input-group-text" id="basic-addon1">Voltaje</span>
          <select class="form-select" aria-label="Default select example" name="voltage2">
            <option value="0.220" readonly>220</option>
            <option value="0.380" readonly>380</option>
          </select>
        </div>
        <div class="input-group mt-3">
          <span class="input-group-text" id="basic-addon1">Tipo de Impedancia</span>
          <select class="form-select" name="impedance2" id="cap_ind" onchange="factorPower3(this)">
            <option selected>Selecciona un tipo</option>
            <option value="inductance">Inductiva</option>
            <option value="capacitance">Capacitiva</option>
          </select>
        </div>
        <div id="factorFP2">
          <div class="input-group mt-3">
              <span class="input-group-text">Factor de Potencia</span>
              <input type="text" class="form-control" placeholder="Ingresa el factor de potencia" name="fp3">
          </div>
          <div class="form-text ps-2" id="basic-addon4">Ingresa el factor de potencia separado por punto.</div>
        </div>
        <div class="input-group mt-2">
              <span class="input-group-text" id="basic-addon1">Potencia por Carga</span>
              <input type="text" class="form-control" placeholder="Ingresa la potencia" aria-label="Username" aria-describedby="basic-addon1" name="power">
        </div>
        <div class="form-text ps-2" id="basic-addon4">La potencia debe ser en watt.</div>
        <div class="input-group mt-2">
          <span class="input-group-text" id="basic-addon3">Distancia de la Carga</span>
          <input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3 basic-addon4" placeholder="Ejemplo: 12.5" name="total_length_ct">
        </div>
        <div class="form-text ps-2" id="basic-addon4">Ingresa el largo total del circuito en metros separado por punto.</div>`;
      }
    }
    }
  });
}


// # --------------------- DELETE LOADS -----------------------------------------------------------

  
function deleteLoad(element) {
  const load_id = element.getAttribute("data_circuit_delete");
  const circuit_id1 = element.getAttribute("data_circuit");
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
        timer: 2000,
        position: 'top',
        showConfirmButton: false
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
          setTimeout(() => {location.reload()}, 1000);
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
        position: 'top',
        timer: 1500,
        showConfirmButton: false
      });
      
      $.ajax({
        url:'/api/delete/circuit',
        method:'POST',
        data:{ circuitv2: circuit_id2},
        success: (data, textStatus, xhr) => {
          setTimeout(() => {location.reload()}, 1000);
        }
      })
    }
  });
}

// -------------------------------- DELETE TGS------------------------------------------------

function deleteTgs() {
  let deleteTgs = document.getElementById("tgs-id").value;
  if (!deleteTgs) {
    Swal.fire({
      title: 'Selecciona un tablero general',
      text: 'Por favor, selecciona un tablero general antes de intentar borrarlo.',
      icon: 'warning',
      position: 'top'
    });
    return;
  }

  Swal.fire({
    title: '¿Estás seguro de que deseas borrar el tablero general?',
    text: 'Si hay circuitos y/o tableros de distribución asociados, ¡también se eliminarán!',
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
        title: 'Borrado Correctamente',
        icon: 'success',
        allowOutsideClick: false,
        position: 'top',
        timer: 1500,
        showConfirmButton: false
      });
      
      $.ajax({
        url:'/api/delete/tgs',
        method:'POST',
        data:{ tgs_delete: deleteTgs},
        success: (data, textStatus, xhr) => {
          setTimeout(() => {location.reload()}, 1000);
        }
      })
    }
  });
}

// -------------------------------- DELETE TDS------------------------------------------------


function deleteTds() {
  let deleteTds = document.getElementById("tds-id").value;

  if (!deleteTds) {
    Swal.fire({
      title: 'Selecciona un tablero de distribución',
      text: 'Por favor, selecciona un tablero de distribución antes de intentar borrarlo.',
      icon: 'warning',
      position: 'top'
    });
    return;
  }
  
  Swal.fire({
    title: '¿Estás seguro de que deseas borrar el tablero de distribución?',
    text: 'Si hay circuitos asociados, ¡también se eliminarán!',
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
        title: 'Borrado Correctamente',
        icon: 'success',
        allowOutsideClick: false,
        position: 'top',
        timer: 1500,
        showConfirmButton: false
      });

      $.ajax({
        url:'/api/delete/tds',
        method:'POST',
        data:{ tds_delete: deleteTds},
        success: (data, textStatus, xhr) => {
          setTimeout(() => {location.reload()}, 1000);
        }
      })
    }
  });
}

// ----------------------- DELETE PROJECT -------------------------------

function deleteProyect() {
  let dePro = document.getElementById('proyect-id').value;
  Swal.fire({
    title: '¿Estás seguro de que deseas borrar el Proyecto?',
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
      $.ajax({
        url:'/api/delete/proyect',
        method:'POST',
        data: {proyect_id: dePro},
        success:(data, textStatus, xhr) => {
          if (data.success == false){
            Swal.fire({
              title: 'No se puede borrar',
              text: 'Hay tableros generales asociados',
              icon: 'error',
              allowOutsideClick: false,
              position: 'top'
            });
            setTimeout(() => {location.reload()}, 5000);
            console.log('no');      
          } 
          else {
            Swal.fire({
              title: 'Borrado Correctamente',
              icon: 'success',
              allowOutsideClick: false,
              position: 'top',
              timer: 1500,
              showConfirmButton: false
            });            
            setTimeout(() => {location.reload()}, 1000);
          }
        }
      })
    }
  })
}


//  --------------- DOWNLOAD EXCEL DISTRIBUTION TABLE --------------

document.getElementById("download-excel-td").addEventListener("click", function(event) {
  event.preventDefault();

  var selectElement = document.getElementById("tds-id");
  var td = selectElement.value;
  
  if (!td) {
    Swal.fire({
      title: 'Selecciona un tablero de distribución',
      text: 'Selecciona un tablero de distribución para descargar el resumén.',
      icon: 'question',
      position: 'top'
    });
    return;
  }

  var url = "/api/excel_tds/" + encodeURIComponent(td);

  fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error('Problemas con el servidor');
      }
      return response.text();
    })
    .then(data => {
      if (data === "No hay circuitos, tablero de distribucíon vacío.") {
        Swal.fire({
          title: 'Tablero de distribución vacío',
          text: 'No hay circuitos en el tablero seleccionado.',
          icon: 'warning',
          position: 'top'
        });
      } else {
        window.location.href = url;
      }
    })
    .catch(error => {
      console.error('tuvimos problemas con fetch:', error);
    });
});
//  --------------- DOWNLOAD EXCEL GENERAL TABLE --------------

function detail_tds(element){
  let detailTd = element.getAttribute("data-td-id");
  console.log(detailTd)
  $.ajax({
    url: "/api/summary-tds/",
    method: "POST",
    data: {id: detailTd},
    success: (data, textStatus, xhr)=> {
      const datailTds1 = document.getElementById("nameCircuitTd");
      const datailTds2 = document.getElementById("detail-tds-circuits-body");
      let modal = '';
      if(data.length > 0){
        data.map(ll => {
          modal += `
          <tr class="border border-dark-subtle text-center" style="font-size: 15px; height: 40px;">
            <td>${ll.total_center}</td>
            <td>${ll.total_active_power_ct}</td>
            <td>${ll.total_current_ct}</td>`;

            if (ll.single_voltage === '0.220') {
              modal += `<td>220</td>`;
            } else {
              modal += `<td>380</td>`;
            }
            modal += `<td>${ll.total_fp}</td>`;
            
            if (ll.td_impedance == "capacitance"){
              modal += `<td>Capacitiva</td>`;
            } else {
              modal += `<td>Inductiva</td>`;
            }

            modal +=`    
            <td>${ll.total_length_ct}</td>
            <td>${ll.vp}</td>
            <td>${ll.method.toUpperCase()}</td>
            <td>${ll.wires}</td>
            <td>${ll.secctionmm2}</td>
            <td>${ll.conduit}</td>
            <td>${ll.breakers}</td>
            <td>${ll.elect_differencial}</td>
          </tr>`;
        })
        datailTds1.innerHTML = "<strong>Cuadro de Resumén " + data[0]['nombre'] + "</strong>";
        datailTds2.innerHTML = modal;
      }
      else {
        modal += `<tr><td><h3>Sin Circuitos</h3></td></tr>`; /* no deberia aparecer porque esta validado en function select_tds */
      }
    }
  })
}


//  --------------- DOWNLOAD EXCEL GENERAL TABLE --------------

document.getElementById("download-excel-tg").addEventListener("click", function(event) {
  event.preventDefault();

  var selectElement = document.getElementById("tgs-id");
  var tg = selectElement.value;
  
  if (!tg) {
    Swal.fire({
      title: 'Selecciona un tablero general',
      text: 'Selecciona un tablero general para descargar el resumén.',
      icon: 'question',
      position: 'top'
    });
    return;
  }

  var url = "/api/excel_tgs/" + encodeURIComponent(tg);

  fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error('Problemas con el servidor');
      }
      return response.text();
    })
    .then(data => {
      if (data === "No hay circuitos, tablero general vacío.") {
        Swal.fire({
          title: 'Tablero general vacío',
          text: 'No hay circuitos en el tablero seleccionado.',
          icon: 'warning',
          position: 'top'
        });
      } else {
        window.location.href = url;
      }
    })
    .catch(error => {
      console.error('tuvimos problemas con fetch:', error);
    });
});

//  --------------------- EDIT NAME TGS --------------------------------------------

  function editNametg(){
  let tgName = document.getElementById("tgs-id").value;
  let modalname = document.getElementById('edit_tg');
    modalname.innerHTML = `
      <div class="input-group my-3">
        <span class="input-group-text" id="basic-addon1" style="width: 200px;">Nuevo Nombre</span>
        <input type="text" class="form-control" placeholder="Nuevo nombre del tablero" aria-label="Username" aria-describedby="basic-addon1" name="name">
      </div>
      <div class="input-group my-3">
        <span class="input-group-text" id="basic-addon1" style="width: 200px;">Nueva Referencia o Tag</span>
        <input type="text" class="form-control" placeholder="Nueva ubicación o identificativo" aria-label="Username" aria-describedby="basic-addon1" name="tag">
        <input type="hidden" name="id" value="${tgName}"></input>
      </div> `; 
}

//  --------------------- EDIT NAME TGS --------------------------------------------

function editNametd(){
  let tdName = document.getElementById("tds-id").value;
  let modalname2 = document.getElementById('edit_td');
    modalname2.innerHTML = `
      <div class="input-group my-3">
        <span class="input-group-text" id="basic-addon1" style="width: 200px;">Nuevo Nombre</span>
        <input type="text" class="form-control" placeholder="Nuevo nombre del tablero" aria-label="Username" aria-describedby="basic-addon1" name="name">
      </div>
      <div class="input-group my-3">
        <span class="input-group-text" id="basic-addon1" style="width: 200px;">Nueva Referencia o Tag</span>
        <input type="text" class="form-control" placeholder="Nueva ubicación o identificativo" aria-label="Username" aria-describedby="basic-addon1" name="tag">
        <input type="hidden" name="id" value="${tdName}"></input>
      </div> `; 
}

  // ------------------- Dinamycs fullcalendar selection -------------------------*/
  
    function viewFullcalendar(element){
      let projectId = element.value
      let daTable = document.getElementById('pro-date');
      let callCalendar = document.getElementById('calCalendar');
      let jobTable = document.getElementById('job_in_proyect');
      let emptyCalendar = document.getElementById('empty-calendar');
      let selectPro = document.getElementById('select-proyect');
      content = "";
      $.ajax({
        url:'/api/info_jobs',
        type:'POST',
        data: {'project_id': projectId},
        success: (data, textStatus, xhr) => {         
        if(data.length > 0 ){
          emptyCalendar.style.display = "none";
          selectPro.style.display = "none";
          daTable.style.display = "block";
          let eventArray = [];
          let eventDescription ="";
          data.forEach(lx => {
            if (String(lx['proyect_id']) === projectId ) {
              console.log(lx['start']);
              console.log(lx['end']);
              let start = moment.utc(lx['start']).format(); // Formato por defecto (ISO 8601)
              let end = moment.utc(lx['end']).format();
              eventArray.push({
                title: lx['title'], 
                start: start, 
                end: end,
              });
              eventDescription += `<h5>${lx.description}</h5>`;
              callCalendar.style.display = "block";
              daTable.style.display = "block";
              let startDate = new Date(lx.start);
              let options = { weekday: 'short', year: '2-digit', month: 'short', day: 'numeric' };
              let formatter = new Intl.DateTimeFormat(navigator.language, options);
              let startDateInLocale = formatter.format(startDate);
              let endDate = new Date(lx.end);
              let endDateInLocale = formatter.format(endDate);
              content += `
              <tr>
                <th scope="row">${lx.title}</th>
                <td>${truncateDescription(lx.description, 15)}</td>
                <td>${startDateInLocale}</td>
                <td>${endDateInLocale}</td>
                <td class="d-flex text-center">
                  <button class="fa-solid fa-eye btn bg-white border" data-view="${lx.description}" data-bs-toggle="modal" data-bs-target="#staticDescription" onclick="viewDesc(this)"></button>
                  <button class="fa-solid fa-pen-to-square btn bg-white border mx-1"></button>
                  <button class="fa-solid fa-trash-can btn bg-white border"></button>
                </td>
              </tr>`;
            jobTable.innerHTML = content;
            function truncateDescription(description, maxLength) { 
              if (description.length > maxLength) {
                return description.substring(0, maxLength) + '...';
              } else {
                return description;
              }
            }
            
          }else {
              console.log('no hay nada');
            }
          });
        //   let hereFullc = document.getElementById('calendar')
        //   const calendar = new FullCalendar.Calendar(hereFullc, {
        //     slotMinTime: '08:00:00',
        //     slotMaxTime:'17:30:00',
        //     businessHours: {
        //       daysOfWeek: [ 1, 2, 3, 4, 5 ],
        //       startTime: '08:00',
        //       endTime: '17:30',
        //     },
        //     locale: 'es',
        //     timeZone: 'UTC',
        //     headerToolbar: {
        //       left: 'dayGridMonth,timeGridWeek,timeGridDay',
        //       center: 'title',
        //       right: 'today prev,next'
        //     },
        //     buttonText: {
        //       today:    'Hoy',
        //       month:    'Mes',
        //       week:     'Semana',
        //       day:      'Día',
        //       list:     'Lista'
        //     },
        //     firstDay: 1,
        //     allDayText: 'Todo el día',
        //     selectable: true,
        //     // editable: true,
        //     events:eventArray,
        //     eventColor: 'gray',
        //     eventDidMount: function(info) {
        //       var today = new Date().getTime();
        //       var eventEnd = new Date(info.event.end).getTime();
        //       var eventStart = new Date(info.event.start).getTime();
      
        //       if (!info.event.end) {
        //           if (eventStart > today) {
        //               info.el.style.backgroundColor = '#FFB347';
        //           }
        //       } else {
        //           if (eventEnd < today) {
        //               info.el.style.backgroundColor = '#77DD77';
        //           }
        //       }
        //     }
        //   });
        // calendar.render();
        } else {
          callCalendar.style.display = "none";
          daTable.style.display = "none";
          emptyCalendar.style.display = "block";
        }
      }
    });
  };



// indicador de carga planning ----//
function mostrarIndicadorDeCarga() {
  Swal.fire({
    title: 'Cargando...',
    allowOutsideClick: false,
    onBeforeOpen: () => {
      Swal.showLoading();
    }
  });
}


// ------- Take one color row in table -----------

function viewDesc(element){
  let lxInfo = document.getElementById('info-view');
  lxInfo.innerHTML = element.getAttribute('data-view');
}

