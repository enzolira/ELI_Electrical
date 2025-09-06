// ------------------------------------------------------------------------------------------------
// ------------------------------------------------------------------------------------------------
// ------------------------------------CREATED OF PROYECT, TGS , TDS, CIRCUITS & LOADS-------------
// ------------------------------------------------------------------------------------------------


// ------------------------------------------------------------------------------------------------

// CIERRE DE SESION POR INACTIVIDAD ------------
// 15 minutos de inactividad y se cierra la sesion

const INACTIVITY_TIME = 15 * 60 * 1000;
const ALERT_TIME =  14 * 60 * 1000;

let inactivityTimer;
let alertTimer;

function resetInactivityTimer() {
    clearTimeout(inactivityTimer);
    clearTimeout(alertTimer);
    alertTimer = setTimeout(showAlert, ALERT_TIME);
    inactivityTimer = setTimeout(logout, INACTIVITY_TIME);
}

function showAlert() {
    Swal.fire({
        title: 'Atención',
        text: 'Tu sesión está a punto de expirar por inactividad. Tienes 1 minuto para seguir activo.',
        icon: 'warning',
        confirmButtonText: 'Continuar',
        position:'top'
    });
}

function logout() {
    Swal.fire({
        title: 'Sesión Expirada',
        text: 'Tu sesión ha expirado debido a inactividad.',
        icon: 'error',
        confirmButtonText: 'OK',
        position:'top'
    }).then(() => {
        window.location.href = '/logout';
    });
}

window.onload = resetInactivityTimer;
document.onmousemove = resetInactivityTimer;
document.onkeydown = resetInactivityTimer;
document.onclick = resetInactivityTimer;
document.onscroll = resetInactivityTimer;



// -------------------------CONFIRMACION CIERRE DE SESION VOLUNTARIAMENTE---------------------------------

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
    // width: '50%',
    position:'top'
  }).then((result) => {
    if (result.isConfirmed){
      window.location.href = event.target.href;
    }
  })
}

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
                let totalActivePowerCt = parseFloat(xl1.total_active_power_ct);
                let formattedTotalActivePowerCt = Number.isInteger(totalActivePowerCt) ? parseInt(totalActivePowerCt) : totalActivePowerCt.toFixed(2);
                let totalCurrentCt = parseFloat(xl1.total_current_ct);
                let formattedTotalCurrentCt = Number.isInteger(totalCurrentCt) ? parseInt(totalCurrentCt) : totalCurrentCt.toFixed(2);
                  content += `
                      <tr class="border-top border-dark-subtle text-center">
                          <td class="border-end border-dark-subtle">${xl1.ref}</td>
                          <td class="border-end border-dark-subtle">${xl1.name}</td>
                          <td class="border-end border-dark-subtle">${xl1.total_center}</td>
                          <td class="border-end border-dark-subtle">${formattedTotalActivePowerCt}</td>
                          <td class="border-end border-dark-subtle">${formattedTotalCurrentCt}</td>`;
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
              let totalActivePowerCt = parseFloat(xl1.total_active_power_ct);
              let formattedTotalActivePowerCt = Number.isInteger(totalActivePowerCt) ? parseInt(totalActivePowerCt) : totalActivePowerCt.toFixed(2);
              let totalCurrentCt = parseFloat(xl1.total_current_ct);
              let formattedTotalCurrentCt = Number.isInteger(totalCurrentCt) ? parseInt(totalCurrentCt) : totalCurrentCt.toFixed(2);    
              content += `
                  <tr class="border-top border-dark-subtle text-center">
                      <td class="border-end border-dark-subtle">${xl1.ref}</td>
                      <td class="border-end border-dark-subtle">${xl1.name}</td>
                      <td class="border-end border-dark-subtle">${xl1.total_center}</td>
                      <td class="border-end border-dark-subtle">${formattedTotalActivePowerCt}</td>
                      <td class="border-end border-dark-subtle">${formattedTotalCurrentCt}</td>`;
              if (xl1.single_voltage === '0.220') {
                  content += `<td class="border-end border-dark-subtle">220</td>`;
              } else {
                  content += `<td class="border-end border-dark-subtle">380</td>`;
              }
              content += `
                      <td><button type="button" class="btn btn-outline-secondary me-2 my-1 btn-sm" onclick="detail_circuit(this)" data-circuit-id="${xl1.circuit_id}" data-bs-toggle="modal" data-bs-target="#staticBackdrop2">Ver</button><button class="btn btn-sm btn-outline-danger my-1" data_circuit_delete2="${xl1.circuit_id}" onclick="deleteCircuit(this)">Borrar</button></td>
                  </tr>`;
              count.push(xl1.circuit_id);
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
                      <button type="button" onclick="detail_tds(this)" class="btn btn-sm btn-outline-secondary mx-2 my-1" style="width: 60%" data-td-id ="${item.td_id}" data-bs-toggle="modal" data-bs-target="#staticBackdrop4">Ver</button>
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
            let totalActivePowerCt = parseFloat(xl.total_active_power_ct);
            let formattedTotalActivePowerCt = Number.isInteger(totalActivePowerCt) ? parseInt(totalActivePowerCt) : totalActivePowerCt.toFixed(2);
            let totalCurrentCt = parseFloat(xl.total_current_ct);
            let formattedTotalCurrentCt = Number.isInteger(totalCurrentCt) ? parseInt(totalCurrentCt) : totalCurrentCt.toFixed(2);
        
            content += 
                `<tr class="border-top border-dark-subtle text-center">
                    <td class="border-end border-dark-subtle">${xl.nameloads}</td>
                    <td class="border-end border-dark-subtle">${xl.name}</td>
                    <td class="border-end border-dark-subtle">${xl.total_center}</td>
                    <td class="border-end border-dark-subtle">${formattedTotalActivePowerCt}</td>
                    <td class="border-end border-dark-subtle">${formattedTotalCurrentCt}</td>`;
            if (xl.single_voltage === '0.220') {
                content += `<td class="border-end border-dark-subtle">220</td>`;
            } else {
                content += `<td class="border-end border-dark-subtle">380</td>`;
            }
            content += `
                    <td>
                        <button type="button" onclick="detail_circuit(this)" class="btn btn-sm btn-outline-secondary me-2 my-1" data-circuit-id="${xl.circuit_id}" data-bs-toggle="modal" data-bs-target="#staticBackdrop2">Ver</button>
                        <button class="btn btn-outline-danger my-1" data_circuit_delete2="${xl.circuit_id}" onclick="deleteCircuit(this)">Borrar</button>
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
        
      // Con esta function acerco los decimales de .00 a nada y .87 los muestra //
      
            function formatNumber(value) {
              let floatValue = parseFloat(value);
              if (Number.isInteger(floatValue)) {
                  return parseInt(floatValue);
              } else {
                  return floatValue.toFixed(2);
              }
          }

        if (data.length > 0) {
          const xl = data[0];
          html += 
              `<tr class="border border-dark-subtle text-center" style="font-size: 15px; height: 40px;">
                  <td>${xl.total_center}</td>
                  <td>${formatNumber(xl.total_active_power_ct)}</td>
                  <td>${formatNumber(xl.total_current_ct)}</td>`;
      
          if (xl.single_voltage === '0.220') {
              html += `<td>220</td>`;
          } else {
              html += `<td>380</td>`;
          }
          html += `<td>${xl.total_fp}</td>`;
      
          if (xl.name_impedance == "capacitance") {
              html += `<td>Capacitiva</td>`;
          } else {
              html += `<td>Inductiva</td>`;
          }
      
          html +=`    
                  <td>${xl.total_length_ct}</td>
                  <td>${xl.vp}</td>
                  <td>${xl.method.toUpperCase()}</td>
                  <td>${xl.wires}</td>
                  <td>${formatNumber(xl.secctionmm2)}</td>
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
                  <td class="border border-dark-subtle">${formatNumber(xl.total_active_power)}</td>
                  <td class="border border-dark-subtle">${formatNumber(xl.total_current)}</td>`;
      
          if (xl.voltage === '0.220') {
              content += `<td class="border border-dark-subtle">220</td>`;
          } else {
              content += `<td class="border border-dark-subtle">380</td>`;
          }
          
          content += `<td class="border border-dark-subtle">
                          <button class="btn btn-sm btn-outline-danger my-1" data_circuit=${xl.circuit_id} data_circuit_delete=${xl.id} onclick="deleteLoad(this)">Borrar</button>
                      </td>
                  </tr>`;
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
          if (textStatus == "success") {
            // var modal = document.getElementById("staticBackdrop2");
            // var modalInstance = bootstrap.Modal.getInstance(modal);
            // modalInstance.hide();
            // var circuitId2 = element.getAttribute("data-circuit-id");
            // detail_circuit(circuitId2);
            setTimeout(() => {location.reload()}, 1500);
          }
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
          setTimeout(() => {location.reload()}, 1500);
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
          setTimeout(() => {location.reload()}, 1500);
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
          setTimeout(() => {location.reload()}, 1500);
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
            setTimeout(() => {location.reload()}, 4000);
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
            setTimeout(() => {location.reload()}, 1500);
          }
        }
      })
    }
  })
}


//  --------------- DOWNLOAD EXCEL DISTRIBUTION TABLE --------------

document.addEventListener('DOMContentLoaded', function() {
  const downloadBtn = document.getElementById("download-excel-td");
  const selectElement = document.getElementById("tds-id");

  // Verificar que los elementos existen
  if (!downloadBtn || !selectElement) {
    return;
  }

  downloadBtn.addEventListener("click", async function(event) {
    event.preventDefault();
    
    const td = selectElement.value.trim();
    
    // Validar selección
    if (!td) {
      if (typeof Swal !== 'undefined') {
        Swal.fire({
          title: 'Selección requerida',
          text: 'Por favor selecciona un tablero de distribución',
          icon: 'warning',
          position: 'top'
        });
      } else {
        alert('Por favor selecciona un tablero de distribución');
      }
      return;
    }

    const url = `/api/excel_tds/${encodeURIComponent(td)}`;
    
    try {
      // Mostrar carga
      if (typeof Swal !== 'undefined') {
        Swal.fire({
          title: 'Generando archivo',
          html: 'Por favor espera...',
          allowOutsideClick: false,
          didOpen: () => Swal.showLoading()
        });
      }

      const response = await fetch(url);
      
      if (!response.ok) {
        throw new Error(`Error ${response.status}: ${response.statusText}`);
      }

      const contentType = response.headers.get('content-type');
      const blob = await response.blob();

      // Ocultar carga
      if (typeof Swal !== 'undefined') Swal.close();

      // Manejar diferentes tipos de respuesta
      if (contentType.includes('application/json')) {
        const data = await response.json();
        if (data.message === "No hay circuitos") {
          Swal.fire({
            title: 'Tablero vacío',
            text: 'El tablero seleccionado no tiene circuitos',
            icon: 'info'
          });
          return;
        }
      } else {
        // Descargar archivo
        const downloadUrl = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = downloadUrl;
        a.download = `cuadro_cargas_${td}_${new Date().toISOString().slice(0,10)}.xlsx`;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(downloadUrl);
        a.remove();
      }
    } catch (error) {
      console.error('Error en la descarga:', error);
      if (typeof Swal !== 'undefined') {
        Swal.fire({
          title: 'Error',
          text: 'No se pudo generar el archivo',
          icon: 'error'
        });
      }
    }
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
      function formatNumber(value) {
        let floatValue = parseFloat(value);
        if (Number.isInteger(floatValue)) {
            return parseInt(floatValue);
        } else {
            return floatValue.toFixed(2);
        }
    }
      const datailTds1 = document.getElementById("nameCircuitTd");
      const datailTds2 = document.getElementById("detail-tds-circuits-body");
      let modal = '';
      if(data.length > 0){
        data.map(ll => {
          modal += `
          <tr class="border border-dark-subtle text-center" style="font-size: 15px; height: 40px;">
            <td>${ll.total_center}</td>
            <td>${formatNumber(ll.total_active_power_ct)}</td>
            <td>${ll.total_current_ct}</td>`;

            if (ll.single_voltage === '0.220') {
              modal += `<td>220</td>`;
            } else {
              modal += `<td>380</td>`;
            }
            modal += `<td>${ll.total_fp}</td>`;
            
            if (ll.name_impedance == "capacitance"){
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

// Esperar a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
  const downloadButton = document.getElementById("download-excel-tg");
  
  if (downloadButton) {
    downloadButton.addEventListener("click", async function(event) {
      event.preventDefault();
      
      // Verificar que SweetAlert está disponible
      if (typeof Swal === 'undefined') {
        console.error('SweetAlert no está cargado');
        alert('Selecciona un tablero general para descargar');
        return;
      }
      
      const selectElement = document.getElementById("tgs-id");
      
      // Verificar que el select existe
      if (!selectElement) {
        console.error('Elemento tgs-id no encontrado');
        Swal.fire({
          title: 'Error',
          text: 'No se encontró el selector de tableros generales',
          icon: 'error'
        });
        return;
      }
      
      const tg = selectElement.value.trim();
      
      if (!tg) {
        Swal.fire({
          title: 'Selecciona un tablero general',
          text: 'Selecciona un tablero general para descargar Cuadro de Carga.',
          icon: 'question',
          position: 'top'
        });
        return;
      }

      const url = "/api/excel_tgs/" + encodeURIComponent(tg);
      
      try {
        // Mostrar loader mientras se procesa
        Swal.fire({
          title: 'Generando archivo',
          html: 'Por favor espera...',
          allowOutsideClick: false,
          didOpen: () => {
            Swal.showLoading();
          }
        });
        
        const response = await fetch(url);
        
        if (!response.ok) {
          throw new Error(`Error HTTP: ${response.status}`);
        }
        
        const contentType = response.headers.get('content-type');
        
        // Manejar diferentes tipos de respuesta
        if (contentType.includes('application/json')) {
          const data = await response.json();
          Swal.close();
          
          if (data.message === "No hay circuitos, tablero general vacío.") {
            Swal.fire({
              title: 'Tablero general vacío',
              text: 'No hay circuitos en el tablero seleccionado.',
              icon: 'warning',
              position: 'top'
            });
          }
          return;
        }
        
        // Si es un archivo, descargarlo
        const blob = await response.blob();
        const downloadUrl = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = downloadUrl;
        a.download = `cuadro_carga_tg_${tg}.xlsx`;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(downloadUrl);
        document.body.removeChild(a);
        
        Swal.close();
        
      } catch (error) {
        console.error('Error en la descarga:', error);
        Swal.fire({
          title: 'Error',
          text: 'Ocurrió un problema al generar el archivo',
          icon: 'error'
        });
      }
    });
  } else {
  }
});

//  --------------------- EDIT NAME TGS --------------------------------------------

// Esperar a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
  const editButton = document.getElementById("edit_name_tg");
  
  if (editButton) {
    editButton.addEventListener("click", function(event) {
      event.preventDefault();
      
      // Verificar que SweetAlert está disponible
      if (typeof Swal === 'undefined') {
        console.error('SweetAlert no está cargado');
        alert('Error: La funcionalidad de alertas no está disponible');
        return;
      }
      
      const selectElement = document.getElementById("tgs-id");
      
      // Verificar que el select existe
      if (!selectElement) {
        console.error('Elemento tgs-id no encontrado');
        Swal.fire({
          title: 'Error',
          text: 'No se encontró el selector de tableros generales',
          icon: 'error'
        });
        return;
      }
      
      const tg_edit = selectElement.value.trim();
      console.log('Tablero seleccionado:', tg_edit);

      if (!tg_edit) {
        Swal.fire({
          title: 'Selecciona un Tablero General',
          text: 'Selecciona un tablero para editarlo.',
          icon: 'question',
          position: 'top'
        });
        return;
      }
      
      try {
        // Generar el contenido del modal
        editNametg(tg_edit);
        
        // Mostrar el modal
        const modalElement = document.getElementById('staticEditNametg');
        if (modalElement) {
          const myModal = new bootstrap.Modal(modalElement);
          myModal.show();
        } else {
          throw new Error('Modal staticEditNametg no encontrado');
        }
      } catch (error) {
        console.error('Error al mostrar el modal:', error);
        Swal.fire({
          title: 'Error',
          text: 'No se pudo cargar el formulario de edición',
          icon: 'error'
        });
      }
    });
  } else {
  }
});

function editNametg(tgName) {
  try {
    const modalname = document.getElementById('edit_tg');
    
    if (!modalname) {
      throw new Error('Elemento edit_tg no encontrado');
    }
    
    // Validar que tgName no esté vacío
    if (!tgName) {
      throw new Error('Nombre del tablero no proporcionado');
    }
    
    modalname.innerHTML = `
      <div class="input-group my-3">
        <span class="input-group-text" id="basic-addon1" style="width: 200px;">Nuevo Nombre</span>
        <input type="text" class="form-control" placeholder="Nuevo nombre del tablero" 
               aria-label="Username" aria-describedby="basic-addon1" name="name" required>
      </div>
      <div class="input-group my-3">
        <span class="input-group-text" id="basic-addon1" style="width: 200px;">Nueva Referencia o Tag</span>
        <input type="text" class="form-control" placeholder="Nueva ubicación o identificativo" 
               aria-label="Username" aria-describedby="basic-addon1" name="tag" required>
        <input type="hidden" name="id" value="${tgName}">
      </div>`;
    
  } catch (error) {
    console.error('Error en editNametg:', error);
    throw error; // Re-lanzar el error para manejarlo en el llamador
  }
}


//  --------------------- EDIT NAME TDS --------------------------------------------

// Esperar a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
  const editButton = document.getElementById("edit_name_td");
  
  // Verificar si el botón existe
  if (!editButton) {
    return;
  }

  editButton.addEventListener("click", function(event) {
    event.preventDefault();
    
    // Verificar que SweetAlert está disponible
    if (typeof Swal === 'undefined') {
      console.error('SweetAlert no está cargado');
      alert('Error: La funcionalidad de alertas no está disponible');
      return;
    }
    
    const selectElement = document.getElementById("tds-id");
    
    // Verificar que el select existe
    if (!selectElement) {
      console.error('Elemento tds-id no encontrado');
      Swal.fire({
        title: 'Error',
        text: 'No se encontró el selector de tableros',
        icon: 'error'
      });
      return;
    }
    
    const td_edit = selectElement.value.trim();
    console.log('Tablero seleccionado para editar:', td_edit);

    if (!td_edit) {
      Swal.fire({
        title: 'Selecciona un Tablero de Distribución',
        text: 'Selecciona un tablero para editarlo.',
        icon: 'question',
        position: 'top',
        timer: 3000
      });
      return;
    }
    
    try {
      // Generar el contenido del modal
      if (!editNametd(td_edit)) {
        throw new Error('Error al generar el formulario de edición');
      }
      
      // Mostrar el modal
      const modalElement = document.getElementById('staticEditNametd');
      if (!modalElement) {
        throw new Error('Modal staticEditNametd no encontrado');
      }
      
      const myModal = new bootstrap.Modal(modalElement);
      myModal.show();
      
    } catch (error) {
      console.error('Error al mostrar el modal de edición:', error);
      Swal.fire({
        title: 'Error',
        text: 'No se pudo cargar el formulario de edición',
        icon: 'error',
        timer: 3000
      });
    }
  });
});

function editNametd(tdName) {
  try {
    if (!tdName) {
      throw new Error('Nombre del tablero no proporcionado');
    }
    
    const modalContainer = document.getElementById('edit_td');
    if (!modalContainer) {
      throw new Error('Contenedor edit_td no encontrado');
    }
    
    modalContainer.innerHTML = `
      <div class="input-group my-3">
        <span class="input-group-text" id="td-name-label" style="width: 200px;">Nuevo Nombre</span>
        <input type="text" class="form-control" placeholder="Nuevo nombre del tablero" 
               aria-label="Nuevo nombre" aria-describedby="td-name-label" name="name" required>
      </div>
      <div class="input-group my-3">
        <span class="input-group-text" id="td-tag-label" style="width: 200px;">Nueva Referencia o Tag</span>
        <input type="text" class="form-control" placeholder="Nueva ubicación o identificativo" 
               aria-label="Nueva referencia" aria-describedby="td-tag-label" name="tag" required>
        <input type="hidden" name="id" value="${tdName}">
      </div>`;
    
    return true;
    
  } catch (error) {
    console.error('Error en editNametd:', error);
    return false;
  }
}

  // ------------------- INFORME DE RECEPCION -------------------------*/

function pisos(element) {
  $.ajax({
    url: '/api/mall',
    method: 'POST',
    data: { mall: element.value },
    success: (data, textStatus, xhr) => {
      let floor1 = document.getElementById("floor-id-1");
      let floor2 = document.getElementById("floor-id-2");
      let local1 = document.getElementById("local-id-1");
      let local2 = document.getElementById("local-id-2");
      let selecContent = document.getElementById("selec-floor");
      let content = "";
      if (Array.isArray(data) && data.length > 0) {
        floor1.style.display = 'none';
        floor2.style.display = 'block';
        local1.style.display = 'block';
        local2.style.display = 'none';
        data.map(el => {
          content += `<option value=${el.id}>${el.piso}</option>`
        });
        selecContent.innerHTML = content;
      }
      else {
        floor1.style.display = 'block';
        floor2.style.display = 'none';
        local1.style.display = 'block';
        local2.style.display = 'none';
      }
    },
    error: (xhr, textStatus, error) => {
      console.log(xhr, textStatus, error);
    },
  });
}


function pisoLocal(element) {
  $.ajax({
    url: '/api/mall',
    method: 'POST',
    data: { mall: element.value },
    success: (data, textStatus, xhr) => {
    let Pisos = document.getElementById("floor");
    let Pisos1 = document.getElementById("floor1");
    let content = "<option selected>-Seleccione el piso-</option>";
    if (Array.isArray(data) && data.length > 0) {
      data.map(eli => {
        content += `<option value=${eli.id}>${eli.piso}</option>`;
      });
      Pisos.innerHTML = content;
      Pisos1.innerHTML = content;
      }
    else {
      content = "<option selected>-Seleccione el piso-</option>";
      }
      Pisos.innerHTML = content;
      Pisos1.innerHTML = content;
    },
    error: (xhr, textStatus, error) => {
      console.log(xhr, textStatus, error);
    },
  });
}


function locales(element) {
  $.ajax({
    url: '/api/floors',
    method: 'POST',
    data: { floor: element.value },
    success: (data, textStatus, xhr) => {
      let local1 = document.getElementById("local-id-1");
      let local2 = document.getElementById("local-id-2");
      let selecLocal = document.getElementById("selec-local");
      let content = "";
      if (Array.isArray(data) && data.length > 0) {
        local1.style.display = 'none';
        local2.style.display = 'block';
        data.map(eli => {
          content += `<option value=${eli.id}>${eli.marca} ${eli.numero}</option>`
        });
        selecLocal.innerHTML = content;
      }
      else {
        local1.style.display = 'block';
        local2.style.display = 'none';
      }
    },
    error: (xhr, textStatus, error) => {
      console.log(xhr, textStatus, error);
    },
  });
}

function locales2(element) {
  $.ajax({
    url: '/api/floors',
    method: 'POST',
    data: { floor: element.value },
    success: (data, textStatus, xhr) => {
      let loCal = document.getElementById("local1");
      let content = "<option selected>-Seleccione un local-</option>";
      if (Array.isArray(data) && data.length > 0) {
        data.map(eli => {
          content += `<option value=${eli.id}>${eli.marca} ${eli.numero}</option>`
        });
        loCal.innerHTML = content;
      }
      else {

      }
      loCal.innerHTML = content;
    },
    error: (xhr, textStatus, error) => {
      console.log(xhr, textStatus, error);
    },
  });
}



// ------------------------------------------------------------------------------------------------------------------------------------