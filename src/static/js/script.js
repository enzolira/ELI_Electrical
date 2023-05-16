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

// ----------- SELECT PROYECTS -----------------------

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
        selectElement.innerHTML = '';
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
        selectElement1.style.display = 'block';
        selectElement2.style.display = 'none';
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
        // const selectElement6 = document.getElementById("h6-circuit2");
        // const selectElement7 = document.getElementById("h5-circuit");
        selectElement3.style.display = 'none';
        selectElement4.style.display = 'block';
        selectElement5.style.display = 'none';
        // selectElement6.style.display = 'block';
        // selectElement7.style.display = 'none';
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
        const selectElement6 = document.getElementById("h6-circuit2");
        const selectElement7 = document.getElementById("h5-circuit");
        divhide1.style.display = 'none';
        divhide2.style.display = 'block';
        divhide3.style.display = 'none';
        divshow4.style.display = 'block';
        selectElement3.style.display = 'none';
        selectElement4.style.display = 'block';
        selectElement5.style.display = 'none';
        selectElement6.style.display = 'block';
        selectElement7.style.display = 'none';
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
      console.log(data[0]);
      if (Array.isArray(data[0]) && data[0].length > 0) {
        // Cambiar el estado de display del select
        console.log(data[0]);
        const selectElement1 = document.getElementById("for-tds");
        const selectElement2 = document.getElementById("h6-tds");
        selectElement2.style.display = 'none';
        selectElement1.style.display = 'block';        
        const selectElement4 = document.getElementById("td-circuit");
        const selectElement5 = document.getElementById("h6-circuit");
        selectElement4.style.display = 'none';
        selectElement5.style.display = 'none';
        tableSelect = document.getElementById("tds-id");
        content = '';
        data[0].map(xl => {
          content += `<option value=${xl.id}>${xl.name}</option>`;
        });
        tableSelect.innerHTML = content;
      } else {
        const selectElement1 = document.getElementById("tg-circuit");
        const selectElement2 = document.getElementById("h6-circuit");
        const selectElement3 = document.getElementById("td-circuit");
        const selectElement6 = document.getElementById("h6-circuit2");
        const selectElement7 = document.getElementById("h5-circuit");
        selectElement1.style.display = 'none';
        selectElement2.style.display = 'block';
        selectElement3.style.display = 'none';
        selectElement6.style.display = 'none';
        selectElement7.style.display = 'block';
        }
      if (Array.isArray(data[1]) && data[1].length > 0) {
        console.log(data[1]);
        const selectElement11 = document.getElementById("tg-circuit");
        const selectElement22 = document.getElementById("h6-circuit");
        const selectElement44 = document.getElementById("td-circuit");
        selectElement11.style.display = 'block';
        selectElement22.style.display = 'none';
        selectElement44.style.display = 'none';
      
        const tableCircuit = document.getElementById("tg-tbody-td");
        let content = '';
      
        data[1].forEach(xl => {
          content += `
            <tr class="border-top border-dark-subtle text-center">
              <td class="border-end border-dark-subtle">${xl.ref}</td>
              <td class="border-end border-dark-subtle">${xl.name}</td>
              <td class="border-end border-dark-subtle">${xl.total_power}</td>
              <td class="border-end border-dark-subtle">${xl.total_current}</td>
              <td class="border-end border-dark-subtle">220</td>
              <td><button class="btn border" onclick="detail_circuit_tds(this)" data-circuit-id="${xl.id}" class="me-2" data-bs-toggle="modal" data-bs-target="#staticBackdrop2">Ver</button><button class="btn border" class="me-2">Editar</button><button class="btn border"  class="me-2">Borrar</button></td>
            </tr>`;
          });

          console.log(content);
          tableCircuit.innerHTML = content;

      } else {
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
  $.ajax({
    url: '/api/circuits_td',
    method: 'POST',
    data: { tgs: tgsSelectedValues, tds: tdsSelectedValues },
    success: (data, textStatus, xhr) => {
      if (Array.isArray(data) && data.length > 0) {
        // Cambiar el estado de display del select
        const selectElement1 = document.getElementById("td-circuit");
        const selectElement2 = document.getElementById("h6-circuit");
        selectElement1.style.display = 'block';
        selectElement2.style.display = 'none';
        const selectElement3 = document.getElementById("tg-circuit");
        const selectElement4 = document.getElementById("h6-circuit");
        selectElement3.style.display = 'none';
        selectElement4.style.display = 'none';
        const tableCircuit = document.getElementById("td-tbody-td")
        content = '';
        data.map(xl => {
          content += 
          `<tr class="border-top border-dark-subtle text-center">
            <td class="border-end border-dark-subtle">${xl.ref}</td>
            <td class="border-end border-dark-subtle">${xl.name}</td>
            <td class="border-end border-dark-subtle">${xl.total_power}</td>
            <td class="border-end border-dark-subtle">${xl.total_current}</td>
            <td class="border-end border-dark-subtle">220</td>
            <td><button class="btn border" onclick="detail_circuit_tds(this)" data-circuit-id="${xl.id}" class="me-2" data-bs-toggle="modal" data-bs-target="#staticBackdrop2">Ver</button><button class="btn border" class="me-2">Editar</button><button class="btn border"  class="me-2">Borrar</button></td>
          </tr>`;
        });
        console.log(content);
        tableCircuit.innerHTML = content;
      } else {
        // Código para cuando data está vacío
        const selectElement1 = document.getElementById("tg-circuit");
        const selectElement2 = document.getElementById("h6-circuit");
        const selectElement4 = document.getElementById("h6-circuit2");
        const selectElement3 = document.getElementById("h5-circuit");
        selectElement1.style.display = 'none';
        selectElement4.style.display = 'none';
        selectElement2.style.display = 'block';
        selectElement3.style.display = 'block';
      }
    },
    error: (xhr, textStatus, error) => {
      console.log(xhr, textStatus, error);
    },
  });
}



function detail_circuit_tds(element) {
  var circuitId = element.getAttribute("data-circuit-id");
  console.log(circuitId);
  $.ajax({
    url: `/api/detail/tds`,
    method: "POST",
    data: { tds: circuitId },
    success: (data, textStatus, xhr) => {
      console.log(data);
      if (textStatus === "success") {
        const nameCircuit = document.getElementById("nameCircuit")
        const detailTable = document.getElementById("detail-circuit");
        content = "";
        data.forEach(ct => {
          content += 
          `<tr class="border border-dark-subtle text-center">
            <td class="border border-dark-subtle">${ct.ref}</td>
            <td class="border border-dark-subtle">${ct.name}</td>
            <td class="border border-dark-subtle">${ct.qty}</td>
            <td class="border border-dark-subtle">${ct.power}</td>
            <td class="border border-dark-subtle">${ct.total_power}</td>
            <td class="border border-dark-subtle">${ct.total_current}</td>`;
        
            if (ct.type_circuit === 'feeder') {
              content += `<td class="border border-dark-subtle">Alimentador</td>`;
            } else {
              content += `<td class="border border-dark-subtle">Subalimentador</td>`;
            }
          content += `
            <td class="border border-dark-subtle">${ct.largo}</td>
            <td class="border border-dark-subtle">${ct.fp}</td>
            <td class="border border-dark-subtle">${ct.vp}</td>
            <td class="border border-dark-subtle">${ct.wires}</td>
            <td class="border border-dark-subtle">${ct.secctionmm2}</td>
            <td class="border border-dark-subtle">${ct.breakers}</td>
            <td class="border border-dark-subtle">${ct.elect_differencial}</td>
          </tr>`;        
        });
        console.log(content);
        console.log(data[0]['ref']);
        detailTable.innerHTML = content;
        nameCircuit.innerHTML = "Circuito: " + data[0]['ref'];
      }
    }
  });
}
