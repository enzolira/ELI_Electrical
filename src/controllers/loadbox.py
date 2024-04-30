from flask import render_template,redirect,session,request, flash, jsonify, url_for , send_file, make_response, url_for
from src import app
from src.models.user import User
from src.models.proyects import Proyect
from src.models.tgs import Tgs
from src.models.circuits import Circuit
from src.models.loads import Load
from src.models.tds import Tds
from src.models.total_tds import Total_tds
from src.controllers import planning
from flask_bcrypt import Bcrypt
import math
import time
import pandas as pd
import io
bcrypt = Bcrypt(app)


#  -------------------------------------------------MAIN PAGE ---------------------------------------------------



@app.route('/loadbox/')
def loadbox():
    if 'user_id' not in session:
        return redirect('/logout')

    data ={'id': session['user_id']}

    user = User.get_by_id(data)
    proyects = Proyect.get_all_proyect_by_user_id(data)
    tgs = Proyect.get_all_tgs_by_proyect_id_and_user_id(data)
    wires= Proyect.get_all_wires()
    return render_template('loadbox.html', user=user, proyects=proyects, tgs=tgs, wires=wires)



#  -------------------------------------------------NEW PROYECTS ---------------------------------------------------



# @app.route('/new_proyect', methods=['POST'])
# def new_proyect():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     data = {
#         'name': request.form['name'],
#         'user_id': session['user_id']
#     }

#     Proyect.save(data)
#     return redirect('/loadbox')



# ------------------------------------------------ADD NEW GENERAL TABLE-------------------------------------------------



@app.route('/add_tgs', methods=['POST'])
def add_tgs():
    if 'user_id' not in session:
        return redirect('/logout')
    
    data = {
        'name': "Tablero " + request.form['name'],
        'tag': request.form['tag'],
        'proyect_id': request.form['proyect_id']
    }
    Tgs.add_tgs(data)
    return redirect('/loadbox')


# ------------------------------------------------ADD NEW DISTRIBUCION TABLE--------------------------------------------



@app.route('/add_tds', methods=['POST'])
def add_tds():
    if 'user_id' not in session:
        return redirect('/logout')
    
    data = {
        'name': "Tablero " + request.form['name'],
        'tag': request.form['tag'],
        'tg_id': request.form['tg_id']
    }
    td_null = Tgs.get_tgs_circuit_tds_null({'tg_id': request.form['tg_id']})

    max_name = 0

    for td in td_null:
        print(td)
        name_value = int(td['name'])
        if name_value > max_name:
            max_name = name_value

    count1 = Tgs.count_tds({'tg_id': request.form['tg_id']})
    
    if max_name and count1:

        td = []
        td = Tds.get_td_by_id({'id':Tds.add_tds(data)})
        for qq in td:
            count = Tgs.get_tds_tgs_circuit({'tg_id':qq['tg_id']})
            print("Aca el if")
            data2 = {
                'name': count[0]['circuits_tg'],
                'ref': qq['name'],
                'tab_secondary': qq["tg_id"],
                'td_id': qq["id"],
                'method': request.form["method"],
                'wires': request.form["type_isolation"],
                'length_from_tg': request.form["length_from_tg"],
            }
            Total_tds.summary_tds(data2)

    elif not max_name or not count1:
        td = []
        td = Tds.get_td_by_id({'id':Tds.add_tds(data)})
        for qq in td:
            count = Tgs.get_tds_tgs_circuit({'tg_id':qq['tg_id']})
            print("Aca el elif")
            data2 = {
                'name': count[0]['circuits_tg'],
                'ref': qq['name'],
                'tab_secondary': qq["tg_id"],
                'td_id': qq["id"],
                'method': request.form["method"],
                'wires': request.form["type_isolation"],
                'length_from_tg': request.form["length_from_tg"],
            }
            Total_tds.summary_tds(data2)

    return redirect('/loadbox')



# ------------------------------------------------ CREATE CIRCUITS-------------------------------------------------------


@app.route('/new_circuit', methods=['POST'])
def new_circuits():

    if 'user_id' not in session:
        return redirect('/logout')
    
    if not Proyect.validate_circuit(request.form):
        return redirect('/loadbox/')


# --------------CALCULOS MONOFASICOS -------

    if float(request.form['single_voltage']) == 0.220:
        data_tg = {}
        data = {}
        data_tg['tg_id'] = request.form['tg_id']
        if 'td_id' in request.form and request.form['td_id']:
            data_tg['td_id'] = request.form['td_id']
        else:
            data_tg["td_id"] = '-Seleccione tablero de distribución-'

        if int(data_tg['tg_id']) > 0 and data_tg['td_id'] == '-Seleccione tablero de distribución-':
            index_num = Tgs.get_tds_tgs_circuit({'tg_id': request.form['tg_id']})
            data = {
                'name': index_num[0]['circuits_tg'] + 1,
                'td_id': None
            }
        else:
            tds_circuit = Tds.get_all_circuits_by_td_id_and_tg_id(data_tg)
            data = {
                'name': tds_circuit[0]['new_circuit_td'],
                'td_id': request.form['td_id']
            }
        data.update({
            'nameloads': request.form['nameloads'],
            'ref': request.form['ref'],
            'method': request.form['method'],
            'single_voltage': request.form['single_voltage'],
            'total_length_ct': request.form['total_length_ct'],
            'tg_id' : request.form['tg_id'],
            'name_impedance': request.form["impedance"],
        })

        if data['name_impedance'] == "capacitance":
            data['total_fp'] = 0.95
            data['qty'] = request.form['qty']
            data['active_power'] = request.form['power']
            total_active_power = round((int(data['qty']) * float(data['active_power']))/1000,2)
            data['total_apparent_power'] = round((total_active_power) / float(data['total_fp']),2)
            data['total_reactive_power'] = round(-1 * ((data['total_apparent_power']) * math.sqrt(1 - data['total_fp']**2)),2)
        else:
            data['total_fp'] = 0.93
            data['qty'] = request.form['qty']
            data['active_power'] = request.form['power']
            total_active_power = round((int(data['qty']) * float(data['active_power']))/1000,2)
            data['total_apparent_power'] = round((total_active_power) / float(data['total_fp']),2)
            data['total_reactive_power'] = round(data['total_apparent_power'] * math.sqrt(1 - data['total_fp']**2),2)

        data['wires'] = request.form['type_isolation']
        data['type_circuit'] = request.form['type_circuit']
        circuit_id = Circuit.add_circuit(data)
        total_current = round(total_active_power/(float(request.form['single_voltage']) * float(data['total_fp'])),2)
        data1 = {'method':data['method'],'total_current':total_current}
        current_by_method= Proyect.current(data1)
        vp = (2 * 0.018 * float(total_current) * float(data['total_length_ct']))/float(current_by_method[0]['secction_mm2'])
        data2 = {}
        data2['circuit_id'] = circuit_id
        if vp < 4.5:                                                            
            current_by_method2 = Proyect.current(data1)
            data2['breakers'] = current_by_method2[0]['disyuntor']
            data2['elect_differencial'] = current_by_method2[0]['diferencial']
            data2['secctionmm2'] = current_by_method2[0]['secction_mm2']
            data2['current_by_method'] = current_by_method2[0][data['method']]
            Circuit.update_method(data2)
            Circuit.update_secctionmm2(data2)
            Circuit.update_breakers(data2)
            Circuit.update_elect_differencial(data2)
            data3 = { 'vp':round((2*0.018*float(data['total_length_ct'])*float(total_current))/float(data2['secctionmm2']),2), 'circuit_id':circuit_id}
            Circuit.update_vp(data3)
            data4 = {'nameloads':data['nameloads'],'qty': data['qty'], 'active_power':data['active_power'], 'total_active_power':total_active_power, 'total_apparent_power':float(data['total_apparent_power']), 'total_reactive_power':float(data['total_reactive_power']),'fp': data['total_fp'], 'impedance': data['name_impedance'],'length': request.form['total_length_ct'],'voltage': data['single_voltage'] , 'total_current': total_current,'circuit_id': circuit_id }
            Load.save(data4)
            Circuit.updated_loads({'circuit_id':circuit_id})
            if data['method'] == 'd1' or data['method'] == 'd2':
                conduit = Circuit.conduit_mono_subte({'secctionmm2':data2['secctionmm2']})
                data5 = {'conduit': conduit[0]['c3'], 'circuit_id':circuit_id}
                Circuit.update_conduit(data5)
            else:
                conduit = Circuit.conduit_mono_normal({'secctionmm2':data2['secctionmm2']})
                data5 = {'conduit': conduit[0]['c3'], 'circuit_id':circuit_id}
                Circuit.update_conduit(data5)
            time.sleep(2)
            return redirect('/loadbox')
        else: 
            allcurrent_by_method = Circuit.vp_real(data1)
            for all_current in allcurrent_by_method:
                print(all_current)
                if float(2 * 0.018 * float(total_current) * float(data['total_length_ct']))/float((all_current['secction_mm2'])) < 4.5:
                    data2['secctionmm2'] = all_current['secction_mm2']
                    data2['current_by_method'] = all_current['method']
                    break

            current_by_method2 = Proyect.current(data1)
            data2['breakers'] = current_by_method2[0]['disyuntor']
            data2['elect_differencial'] = current_by_method2[0]['diferencial']
            Circuit.update_method(data2)
            Circuit.update_secctionmm2(data2)
            Circuit.update_breakers(data2)
            Circuit.update_elect_differencial(data2)
            data3 = { 'vp':round((2*0.018*float(data['total_length_ct'])*float(total_current))/float(data2['secctionmm2']),2), 'circuit_id':circuit_id}
            Circuit.update_vp(data3)
            print(data['name_impedance'])
            data4 = {'nameloads':data['nameloads'],'qty': data['qty'], 'active_power':data['active_power'], 'total_active_power':total_active_power, 'total_apparent_power':float(data['total_apparent_power']), 'total_reactive_power':float(data['total_reactive_power']),'fp': data['total_fp'], 'impedance': data['name_impedance'], 'voltage': data['single_voltage'] , 'length': request.form['total_length_ct'], 'total_current': total_current,'circuit_id': circuit_id}
            Load.save(data4)
            Circuit.updated_loads({'circuit_id':circuit_id})
            if data['method'] == 'd1' or data['method'] == 'd2':
                conduit = Circuit.conduit_mono_subte({'secctionmm2':data2['secctionmm2']})
                data5 = {'conduit': conduit[0]['c3'], 'circuit_id':circuit_id}
                Circuit.update_conduit(data5)
            else:
                conduit = Circuit.conduit_mono_normal({'secctionmm2':data2['secctionmm2']})
                data5 = {'conduit': conduit[0]['c3'], 'circuit_id':circuit_id}
                Circuit.update_conduit(data5)
            print('funciona por fin 220')
        time.sleep(2)
        return redirect('/loadbox')


# ------------------ CALCULOS TRIFASICOS --------------------
    else:
        data_tg = {}
        data = {}
        data_tg['tg_id'] = request.form['tg_id']
        if 'td_id' in request.form and request.form['td_id']:
            data_tg['td_id'] = request.form['td_id']
        else:
            data_tg["td_id"] = '-Seleccione tablero de distribución-'

        if int(data_tg['tg_id']) > 0 and data_tg['td_id'] == '-Seleccione tablero de distribución-':
            index_num = Tgs.get_tds_tgs_circuit({'tg_id': request.form['tg_id']})
            data = {
                'name': index_num[0]['circuits_tg'] + 1,
                'td_id': None
            }
        else:
            tds_circuit = Tds.get_all_circuits_by_td_id_and_tg_id(data_tg)
            data = {
                'name': tds_circuit[0]['new_circuit_td'],
                'td_id': request.form['td_id']
            }

        data.update({
            'nameloads': request.form['nameloads'],
            'ref': request.form['ref'],
            'method': request.form['method'],
            'single_voltage': request.form['single_voltage'],
            'total_length_ct': request.form['total_length_ct'],
            'name_impedance': request.form['impedance'],
            'total_fp': request.form['fp'],
            'tg_id' : request.form['tg_id']
        })
        print(data['total_fp'])
        if data['name_impedance'] == "capacitance":
            data['qty'] = request.form['qty']
            data['active_power'] = request.form['power']
            total_active_power = round((int(data['qty']) * float(data['active_power']))/1000,2)
            data['total_apparent_power'] = round((total_active_power) / float(request.form['fp']),2)
            data['total_reactive_power'] = round(-1 * ((data['total_apparent_power']) * math.sqrt(1 - float(request.form['fp'])**2)),2)
        else:
            data['qty'] = request.form['qty']
            data['active_power'] = request.form['power']
            total_active_power = round((int(data['qty']) * float(data['active_power']))/1000,2)
            data['total_apparent_power'] = round((total_active_power) / float(data['total_fp']),2)
            data['total_reactive_power'] = round(data['total_apparent_power'] * math.sqrt(1 - float(request.form['fp'])),2)

        data['wires'] = request.form['type_isolation']
        data['type_circuit'] = request.form['type_circuit']
        circuit_id = Circuit.add_circuit(data)
        total_current = round(total_active_power/(float(request.form['single_voltage']) * math.sqrt(3) * float(request.form['fp'])),2)
        data1 = {'method':data['method'],'total_current':total_current}
        current_by_method= Proyect.current_tri(data1)
        vp = (0.018 * float(total_current) * float(data['total_length_ct']))/float(current_by_method[0]['secction_mm2'])
        data2 = {}
        data2['circuit_id'] = circuit_id                                              
        if vp < 4.5:
            current_by_method2 = Proyect.current_tri(data1)
            data2['secctionmm2'] = current_by_method2[0]['secction_mm2']
            data2['current_by_method'] = current_by_method2[0][data['method']]
            data2['breakers'] = current_by_method2[0]['disyuntor']
            data2['elect_differencial'] = current_by_method2[0]['diferencial']
            Circuit.update_method(data2)
            Circuit.update_secctionmm2(data2)
            Circuit.update_breakers(data2)
            Circuit.update_elect_differencial(data2)
            data3 = { 'vp':round((0.018*float(data['total_length_ct'])*float(total_current))/float(data2['secctionmm2']),2), 'circuit_id':circuit_id}
            Circuit.update_vp(data3)
            data4 = {'nameloads':data['nameloads'],'qty': data['qty'], 'active_power':data['active_power'], 'total_active_power':total_active_power, 'total_apparent_power':float(data['total_apparent_power']), 'total_reactive_power':float(data['total_reactive_power']),'fp':float(data['total_fp']), 'impedance': data['name_impedance'], 'voltage': data['single_voltage'] , 'length': request.form['total_length_ct'], 'total_current': total_current,'circuit_id': circuit_id}
            Load.save(data4)
            Circuit.updated_loads({'circuit_id':circuit_id})
            if data['method'] == 'd1' or data['method'] == 'd2':
                print(data['method'])
                conduit = Circuit.conduit_tri_subte({'secctionmm2':data2['secctionmm2']})
                data5 = {'conduit': conduit[0]['c5'], 'circuit_id':circuit_id}
                Circuit.update_conduit(data5)
            else:
                conduit = Circuit.conduit_tri_normal({'secctionmm2':data2['secctionmm2']})
                data5 = {'conduit': conduit[0]['c5'], 'circuit_id':circuit_id}
                Circuit.update_conduit(data5)
            print('funciona por fin 380')
            time.sleep(2)
            return redirect('/loadbox')
        else: 
            allcurrent_by_method = Circuit.vp_real(data1)
            for all_current in allcurrent_by_method:
                if float(0.018 *float(total_current) * float(data['total_length_ct']))/float((all_current['secction_mm2'])) < 4.5:
                    data2['current_by_method'] =  all_current['method']
                    data2['secctionmm2'] = all_current['secction_mm2']
                    break
                                                          
            current_by_method2 = Proyect.current_tri(data1)
            data2['current_by_method'] = current_by_method2[0][data['method']]
            data2['breakers'] = current_by_method2[0]['disyuntor']
            data2['elect_differencial'] = current_by_method2[0]['diferencial']
            Circuit.update_method(data2)
            Circuit.update_secctionmm2(data2)
            Circuit.update_breakers(data2)
            Circuit.update_elect_differencial(data2)
            data3 = { 'vp':round((0.018*float(data['total_length_ct'])*float(total_current))/float(data2['secctionmm2']),2), 'circuit_id':circuit_id}
            Circuit.update_vp(data3)
            data4 = {'nameloads':data['nameloads'],'qty': data['qty'], 'active_power':data['active_power'], 'total_active_power':total_active_power, 'total_apparent_power':float(data['total_apparent_power']), 'total_reactive_power':float(data['total_reactive_power']),'fp':float(data['total_fp']), 'impedance': data['name_impedance'], 'voltage': data['single_voltage'] , 'length': request.form['total_length_ct'], 'total_current': total_current,'circuit_id': circuit_id}
            Load.save(data4)
            Circuit.updated_loads({'circuit_id':circuit_id})
            if data['method'] == 'd1' or data['method'] == 'd2':
                conduit = Circuit.conduit_tri_subte({'secctionmm2':data2['secctionmm2']})
                data5 = {'conduit': conduit[0]['c5'], 'circuit_id':circuit_id}
                Circuit.update_conduit(data5)
            else:
                conduit = Circuit.conduit_tri_normal({'secctionmm2':data2['secctionmm2']})
                data5 = {'conduit': conduit[0]['c5'], 'circuit_id':circuit_id}
                Circuit.update_conduit(data5)
        print('funciona por fin 380')
        time.sleep(2)
        return redirect('/loadbox')



# ---------------------------------------------- AJAX ID CIRCUITS----------------------------------------------------------------


@app.route('/api/tgs', methods=['POST'])
def get_tgs():
    proyect = request.form['proyect']
    tgs1 = Tgs.get_tgs_by_project({'proyect_id': proyect})
    # data_tgs = []
    # for dd in tgs1:
    #     data_tgs.append( Tgs.all_circuits_by_tg({'tg_id':dd['id'] }))
    # data_list = [lst for lst in data_tgs if lst]
    # print(data_list)
    # df = pd.DataFrame.from_records(sum(data_list, []))
    # print(df)
    # # Exportar DataFrame a un archivo Excel
    # # df.to_excel('datos.xlsx', index=False)
    return jsonify(tgs1)


@app.route('/api/tds', methods=['POST'])
def get_tds():
    tg_id = request.form['tgs']
    circuit_tg = Circuit.get_all_circuits_by_tg_id({'tg_id':tg_id})
    tgs = Tds.get_all_tds_by_tg_id({'tg_id':tg_id})
    data2 = {}
    total_tds = []
    info_tds = []
    test_1 = []
    test_2 = []
    test_tds = Total_tds.get_all_total_tds()

    for ss in test_tds:
        if ss['total_current_ct']:
            print(ss['single_voltage'])
            # ---------------- VP MONOFASICO ---------------
            if float(ss['single_voltage']) == 0.220:
                data1 = {'method':ss['method'],'total_current':ss['total_current_ct']}
                current_by_method= Proyect.current(data1)
                vp = round(2 * 0.018 * float(ss['total_current_ct']) * float(ss['length_from_tg'])/float(current_by_method[0]['secction_mm2']),2)
                print(vp)
                data2 = {}
                data2['td_id'] = ss['td_id']
                if vp < 4.5:                                                            
                    current_by_method2 = Proyect.current(data1)
                    data2['breakers'] = current_by_method2[0]['disyuntor']
                    data2['elect_differencial'] = current_by_method2[0]['diferencial']
                    data2['secctionmm2'] = current_by_method2[0]['secction_mm2']
                    data2['current_by_method'] = current_by_method2[0][ss['method']]
                    Total_tds.update_method_total_td(data2)
                    Total_tds.update_secctionmm2_total_td(data2)
                    Total_tds.update_breakers_total_td(data2)
                    Total_tds.update_elect_differencial_total_td(data2)
                    Total_tds.update_vp_td({'vp': vp , 'td_id': ss['td_id']})
                    if ss['method'] == 'd1' or ss['method'] == 'd2':
                        conduit = Circuit.conduit_mono_subte({'secctionmm2':data2['secctionmm2']})
                        print(conduit)
                        datos = {'conduit': conduit[0]['c3'], 'td_id':ss['td_id']}
                        Total_tds.update_conduit_total_td(datos)
                    else:
                        conduit = Circuit.conduit_mono_normal({'secctionmm2':data2['secctionmm2']})
                        datos2 = {'conduit': conduit[0]['c3'], 'td_id':ss['td_id']}
                        Total_tds.update_conduit_total_td(datos2)
                else:
                    allcurrent_by_method = Circuit.vp_real(data1)
                    for all_current in allcurrent_by_method:
                        if float(2 * 0.018 * float(ss['total_current_ct']) * float(ss['length_from_tg']))/float(all_current['secction_mm2']) < 4.5:
                            data2['secctionmm2'] = all_current['secction_mm2']
                            data2['current_by_method'] = all_current['method']
                            break

                    current_by_method2 = Proyect.current(data1)
                    data2['breakers'] = current_by_method2[0]['disyuntor']
                    data2['elect_differencial'] = current_by_method2[0]['diferencial']
                    Total_tds.update_method_total_td(data2)
                    Total_tds.update_secctionmm2_total_td(data2)
                    Total_tds.update_breakers_total_td(data2)
                    Total_tds.update_elect_differencial_total_td(data2)
                    vp_new = round(2 * 0.018 * float(ss['total_current_ct']) * float(ss['length_from_tg'])/float(data2['secctionmm2']),2)
                    Total_tds.update_vp_td({'vp': vp_new , 'td_id': ss['td_id']})
                    if ss['method'] == 'd1' or ss['method'] == 'd2':
                        conduit = Circuit.conduit_mono_subte({'secctionmm2':data2['secctionmm2']})
                        datos3 = {'conduit': conduit[0]['c3'], 'td_id':ss['td_id']}
                        Total_tds.update_conduit_total_td(datos3)
                    else:
                        conduit = Circuit.conduit_mono_normal({'secctionmm2':data2['secctionmm2']})
                        datos4 = {'conduit': conduit[0]['c3'], 'td_id':ss['td_id']}
                        Total_tds.update_conduit_total_td(datos4)
                print('actualizado total_tds 220')

            # ---------------- VP TRIFASICO ---------------
            else:
                data1 = {'method':ss['method'],'total_current':ss['total_current_ct']}
                current_by_method= Proyect.current_tri(data1)
                vp = round(0.018 * float(ss['total_current_ct']) * float(ss['length_from_tg'])/float(current_by_method[0]['secction_mm2']),2)
                data2 = {}
                data2['td_id'] = ss['td_id']
                if vp < 4.5:                                                            
                    current_by_method2 = Proyect.current_tri(data1)
                    data2['breakers'] = current_by_method2[0]['disyuntor']
                    data2['elect_differencial'] = current_by_method2[0]['diferencial']
                    data2['secctionmm2'] = current_by_method2[0]['secction_mm2']
                    data2['current_by_method'] = current_by_method2[0][ss['method']]
                    Total_tds.update_method_total_td(data2)
                    Total_tds.update_secctionmm2_total_td(data2)
                    Total_tds.update_breakers_total_td(data2)
                    Total_tds.update_elect_differencial_total_td(data2)
                    Total_tds.update_vp_td({'vp': vp , 'td_id': ss['td_id']})
                    if ss['method'] == 'd1' or ss['method'] == 'd2':
                        conduit = Circuit.conduit_tri_subte({'secctionmm2':data2['secctionmm2']})
                        datos5 = {'conduit': conduit[0]['c5'], 'td_id':ss['td_id']}
                        Total_tds.update_conduit_total_td(datos5)
                    else:
                        conduit = Circuit.conduit_tri_normal({'secctionmm2':data2['secctionmm2']})
                        datos6 = {'conduit': conduit[0]['c5'], 'td_id':ss['td_id']}
                        Total_tds.update_conduit_total_td(datos6)
                else:
                    allcurrent_by_method = Total_tds.vp_real(data1)
                    for all_current in allcurrent_by_method:
                        print(all_current)
                        if float(0.018 * float(ss['total_current_ct']) * float(ss['length_from_tg']))/float(all_current['secction_mm2']) < 4.5:
                            data2['secctionmm2'] = all_current['secction_mm2']
                            data2['current_by_method'] = all_current['method']
                            break

                    current_by_method2 = Proyect.current_tri(data1)
                    data2['breakers'] = current_by_method2[0]['disyuntor']
                    data2['elect_differencial'] = current_by_method2[0]['diferencial']
                    Total_tds.update_method_total_td(data2)
                    Total_tds.update_secctionmm2_total_td(data2)
                    Total_tds.update_breakers_total_td(data2)
                    Total_tds.update_elect_differencial_total_td(data2)
                    vp_new = round(0.018 * float(ss['total_current_ct']) * float(ss['length_from_tg'])/float(current_by_method2[0]['secction_mm2']),2)
                    Total_tds.update_vp_td({'vp': vp_new , 'td_id': ss['td_id']})
                    if ss['method'] == 'd1' or ss['method'] == 'd2':
                        conduit = Circuit.conduit_tri_subte({'secctionmm2':data2['secctionmm2']})
                        datos7 = {'conduit': conduit[0]['c5'], 'td_id':ss['td_id']}
                        Total_tds.update_conduit_total_td(datos7)
                    else:
                        conduit = Circuit.conduit_tri_normal({'secctionmm2':data2['secctionmm2']})
                        datos8 = {'conduit': conduit[0]['c5'], 'td_id':ss['td_id']}
                        Total_tds.update_conduit_total_td(datos8)
                print('actualizado total_tds 380')
        else:
            pass
        test_1.append(ss)

    for jj in tgs:
        data2['td_id'] = jj['id']
        data2['tg_id'] = jj['tg_id']
        info_tds.append(Circuit.detail_total_circuits_by_td_id(data2))

    print("-------------")
    for ll in info_tds:
        for rr in ll:
            test_2.append(rr)
            if rr:
                all_impedance = Circuit.all_name_impedance({'td_id':rr['td_id']})
                # ---UPDATE IMPEDANCE -----
                count_cap = 0
                count_ind = 0
                for uu in all_impedance:
                    if uu["name_impedance"] == "capacitance":
                        count_cap += 1
                    else:
                        count_ind += 1
                    if count_cap >= count_ind:
                        if rr['all_fp'] >= 0.95 and (rr['total_reactive_power_ct'] < 0 or rr['total_reactive_power_ct'] > 0):
                            print("no hay multa cap")
                        elif 0.95 > rr['all_fp'] >= 0.93 and rr['total_reactive_power_ct'] > 0:
                            print("hay multa cap 1")
                        else:
                            print("hay multa cap revisar armonicos 2")
                        Total_tds.update_td_impedance({'td_impedance': 'capacitance', 'td_id': rr['td_id']})
                    else:
                        if 0.95 > rr['all_fp'] >= 0.93 and rr['total_reactive_power_ct'] < 0:
                            print("hay multa cap 3")
                            Total_tds.update_td_impedance({'td_impedance': 'capacitance', 'td_id': rr['td_id']})
                        else:
                            print("no hay multa inductiva")
                        Total_tds.update_td_impedance({'td_impedance': 'inductance', 'td_id': rr['td_id']})
            else:
                pass
                # ---------- FIN UPDATE ------------------- 
    print("-------------")

    for dict_1, dict_2 in zip(test_1, test_2):
        total_center_1 = dict_1.get('total_center')
        total_center_2 = dict_2.get('total_center')


        if total_center_1 == total_center_2:
            print(f"Los valores de 'total_center' son iguales para '{dict_1['ref']}' y '{dict_2['ref']}': {total_center_1}, {dict_1['name']}")

        else:
            print(f"Valor en test_1 ({dict_1['ref']}): {total_center_1}")
            print(f"Valor en test_2 ({dict_2['ref']}): {total_center_2}")
            if total_center_1 != total_center_2:
                print("Valor diferente en test_2:")
                Total_tds.update_total_tds(dict_2)
            else:
                print("Valor diferente en test_1:")
                Total_tds.update_total_tds(dict_1)
        
    
    result = Total_tds.get_all_total_tds_by_tg_id({'tab_secondary':tg_id})
    if result:
        total_tds.append(result)
    print("---------------")

    return jsonify(tgs, circuit_tg, total_tds)


@app.route('/api/circuits_td', methods=['POST'])
def get_all_circuits_by_tds():

    tgs_values = request.form.getlist('tgs[]')
    tds_values = request.form.getlist('tds[]')

    data = {
        'tg_id': tgs_values,
        'td_id': tds_values
    }
    circuit_td = {}
    if data['td_id'] and data['tg_id']:
        circuit_td = Circuit.get_all_circuit_and_tds_by_tg(data)
    else:
        pass
    return jsonify(circuit_td)

# --------------------- FROM AJAX ABOUT DETAIL CIRCUITS BY TDS AND TGS -----------------------------------------------------------

@app.route('/api/detail', methods=['POST'])
def detai_circuit_tds():
    circuit_id = request.form['circuit']
    circuitos = Circuit.detail_circuit_and_loads_by_id({'circuit_id': circuit_id})
    return jsonify(circuitos)


@app.route('/add_load', methods=['POST'])
def add_loads():
    circuit = Circuit.detail_circuit_and_loads_by_id({'circuit_id': request.form['circuit_id']})

# ------- ADD LOADS IN CIRCUITS MONOPHASE -----------------

    if float(circuit[0]['single_voltage']) == 0.220:
        load = {
            'nameloads': request.form['nameloads'],
            'qty': request.form['qty'],
            'circuit_id': request.form['circuit_id'],
            'active_power': request.form['power'],
            'impedance': request.form['impedance'],
            'length': request.form['total_length_ct'],
            'voltage': request.form['voltage']
        }
        print(f" la tension de la carga es: {request.form['voltage']}")
        if load["impedance"] == "capacitance":
            load['fp'] = 0.95
            total_active_power = round(float((load['qty'])) * float(load['active_power'])/1000,2)
            load['total_active_power'] = total_active_power
            load['total_apparent_power'] = round(total_active_power / float(load["fp"]),2)
            load['total_reactive_power'] = round(-1 * (float(load["total_apparent_power"]) * math.sqrt(1 - load['fp']**2)),2)
        else:
            load['fp'] = 0.93
            total_active_power = round(float((load['qty'])) * float(load['active_power'])/1000,2)
            load['total_active_power'] = total_active_power
            load['total_apparent_power'] = round(total_active_power / float(load["fp"]),2)
            load['total_reactive_power'] = round(float(load["total_apparent_power"]) * math.sqrt(1 - load['fp']**2),2)

        total_current = round(total_active_power/(float(data['voltage']) * float(load['fp'])),2)
        load['total_current'] = total_current
        Load.save(load)
        Circuit.updated_loads({'circuit_id': request.form['circuit_id']})

# ---------------------- CALCULO IMPEDANCIA Y FP ----------------------------------------

        new_total_fp = Circuit.new_total_fp({'id': request.form['circuit_id']})
        print(f" el valor de total_fp es {new_total_fp[0]['power_factor']}")
        Circuit.update_total_fp({'id': request.form['circuit_id'], 'new_total_fp':new_total_fp[0]['power_factor']})
        all_impedance = Load.all_impedance({'circuit_id': request.form['circuit_id']})
        count_cap = 0
        count_ind = 0
        for uu in all_impedance:
            if uu["impedance"] == "capacitance":
                count_cap += 1
            else:
                count_ind += 1

        if count_cap >= count_ind:
            if new_total_fp[0]['power_factor'] >= 0.95:
                if load['total_reactive_power'] < 0:
                    print("no hay multa cap 1")
                else:
                    print("no hay multa cap 2")
            elif 0.95 > new_total_fp[0]['power_factor'] >= 0.93:
                if load['total_reactive_power'] > 0:
                    print("hay multa cap 1")
                else:
                    print("hay multa cap revisar armonicos 2")
            Circuit.update_name_impedance({'name_impedance': 'capacitance', 'id': request.form['circuit_id']})
        else:
            if new_total_fp[0]['power_factor'] >= 0.93:
                if load['total_reactive_power'] < 0:
                    print("hay multa cap 3")
                else:
                    print("no hay multa cap aun que hay mas ind")
                Circuit.update_name_impedance({'name_impedance': 'capacitance', 'id': request.form['circuit_id']})
            else:
                print("hay multa cap revisar armonicos 2")
                Circuit.update_name_impedance({'name_impedance': 'inductance', 'id': request.form['circuit_id']})


# ---------------------------------------------------------------------------------------
        Newtotal_current_ct = Circuit.detail_circuit_and_loads_by_id({'circuit_id': request.form['circuit_id']})
        data = {
            'method':circuit[0]['method'],
            'total_current': Newtotal_current_ct[0]['total_current_ct']
        }
        vp = round((2 * 0.018 * float(Newtotal_current_ct[0]['total_current_ct']) * float(Newtotal_current_ct[0]['total_length_ct']))/float(Newtotal_current_ct[0]['secctionmm2']),2)
        data2 = {}
        data2['circuit_id'] = request.form['circuit_id']                                                     
        if vp < 4.5:
            current_by_method2 = Proyect.current(data)
            data2['breakers'] = current_by_method2[0]['disyuntor']
            data2['elect_differencial'] = current_by_method2[0]['diferencial']
            data2['secctionmm2'] = current_by_method2[0]['secction_mm2']
            data2['current_by_method'] = current_by_method2[0][data['method']]
            Circuit.update_method(data2)
            Circuit.update_secctionmm2(data2)
            Circuit.update_breakers(data2)
            Circuit.update_elect_differencial(data2)
            data3 = { 'vp':round((2*0.018*float(Newtotal_current_ct[0]['total_length_ct'])*float(Newtotal_current_ct[0]['total_current_ct']))/float(data2['secctionmm2']),2), 'circuit_id':request.form['circuit_id']}
            Circuit.update_vp(data3)
            Circuit.updated_loads({'circuit_id': request.form['circuit_id']})
            if Newtotal_current_ct[0]['method'] == 'd1' or Newtotal_current_ct[0]['method'] == 'd2':
                conduit = Circuit.conduit_mono_subte({'secctionmm2':data2['secctionmm2']})
                data5 = {'conduit': conduit[0]['c3'], 'circuit_id':request.form['circuit_id']}
                Circuit.update_conduit(data5)
                return redirect('/loadbox/')
            else:
                conduit = Circuit.conduit_mono_normal({'secctionmm2':data2['secctionmm2']})
                data5 = {'conduit': conduit[0]['c3'], 'circuit_id':request.form['circuit_id']}
                Circuit.update_conduit(data5)
            print('funciona por fin 220')
            return redirect('/loadbox')
        else: 
            allcurrent_by_method = Circuit.vp_real(data)
            for all_current in allcurrent_by_method:
                print(all_current)
                if float(2 * 0.018 * float(Newtotal_current_ct[0]['total_current_ct']) * float(Newtotal_current_ct[0]['total_length_ct']))/float((all_current['secction_mm2'])) < 4.5:
                    data2['secctionmm2'] = all_current['secction_mm2']
                    data2['current_by_method'] = all_current['method']
                    break
                                                             
        current_by_method2 = Proyect.current(data)
        data2['breakers'] = current_by_method2[0]['disyuntor']
        data2['elect_differencial'] = current_by_method2[0]['diferencial']
        Circuit.update_method(data2)
        Circuit.update_secctionmm2(data2)
        Circuit.update_breakers(data2)
        Circuit.update_elect_differencial(data2)
        data3 = { 'vp':round((2*0.018*float(Newtotal_current_ct[0]['total_length_ct'])*float(Newtotal_current_ct[0]['total_current_ct']))/float(data2['secctionmm2']),2), 'circuit_id':request.form['circuit_id']}
        Circuit.update_vp(data3)
        Circuit.updated_loads({'circuit_id': request.form['circuit_id']})
        if Newtotal_current_ct[0]['method'] == 'd1' or Newtotal_current_ct[0]['method'] == 'd2':
            conduit = Circuit.conduit_mono_subte({'secctionmm2':data2['secctionmm2']})
            data5 = {'conduit': conduit[0]['c3'], 'circuit_id':request.form['circuit_id']}
            Circuit.update_conduit(data5)
            return redirect('/loadbox/')
        else:
            conduit = Circuit.conduit_mono_normal({'secctionmm2':data2['secctionmm2']})
            data5 = {'conduit': conduit[0]['c3'], 'circuit_id':request.form['circuit_id']}
            Circuit.update_conduit(data5)
        print('funciona por fin 220')
        return redirect('/loadbox')

# ------- ADD LOADS IN CIRCUITS TRIPHASE -----------------
    else:
        print("aca estamos")
# ------ 380/220-------
        voltage = request.form["voltage2"]
        print(voltage)
        load = {
        'nameloads': request.form['nameloads'],
        'qty': request.form['qty'],
        'circuit_id': request.form['circuit_id'],
        'active_power': request.form['power'],
        'impedance': request.form['impedance2'],
        'length': request.form['total_length_ct'],
        'voltage': voltage
        }

        if voltage == "0.220":
            if load['impedance'] == "capacitance":
                load['fp'] = 0.95
                total_active_power = round((int(load['qty']) * float(load['active_power']))/1000,2)
                load['total_active_power'] = total_active_power
                load['total_apparent_power'] = round((total_active_power) / float(load['fp']),2)
                load['total_reactive_power'] = round(-1 * ((load['total_apparent_power']) * math.sqrt(1 - float(load['fp'])**2)),2)
            else:
                load['fp'] = 0.93
                total_active_power = round((int(load['qty']) * float(load['active_power']))/1000,2)
                load['total_active_power'] = total_active_power
                load['total_apparent_power'] = round((total_active_power) / float(load['fp']),2)
                load['total_reactive_power'] = round(load['total_apparent_power'] * math.sqrt(1 - float(load['fp'])),2)
        
            total_current = round(total_active_power/(math.sqrt(3) * float(float(voltage)) * float(load['fp'])),2)
            load['total_current'] = total_current
            Load.save(load)
            Circuit.updated_loads({'circuit_id': request.form['circuit_id']})

# ---------------------- CALCULO IMPEDANCIA Y FP ----------------------------------------

            new_total_fp = Circuit.new_total_fp({'id': request.form['circuit_id']})
            print(f" el valor de total_fp es {new_total_fp[0]['power_factor']}")
            Circuit.update_total_fp({'id': request.form['circuit_id'], 'new_total_fp':new_total_fp[0]['power_factor']})
            all_impedance = Load.all_impedance({'circuit_id': request.form['circuit_id']})
            count_cap = 0
            count_ind = 0
            for uu in all_impedance:
                if uu["impedance"] == "capacitance":
                    count_cap += 1
                else:
                    count_ind += 1

            if count_cap >= count_ind:
                if new_total_fp[0]['power_factor'] >= 0.95:
                    if load['total_reactive_power'] < 0:
                        print("no hay multa cap 1")
                    else:
                        print("no hay multa cap 2")
                elif 0.95 > new_total_fp[0]['power_factor'] >= 0.93:
                    if load['total_reactive_power'] > 0:
                        print("hay multa cap 1")
                    else:
                        print("hay multa cap revisar armonicos 2")
                Circuit.update_name_impedance({'name_impedance': 'capacitance', 'id': request.form['circuit_id']})
            else:
                if new_total_fp[0]['power_factor'] >= 0.93:
                    if load['total_reactive_power'] < 0:
                        print("hay multa cap 3")
                    else:
                        print("no hay multa cap aun que hay mas ind")
                    Circuit.update_name_impedance({'name_impedance': 'capacitance', 'id': request.form['circuit_id']})
                else:
                    print("hay multa cap revisar armonicos 2")
                    Circuit.update_name_impedance({'name_impedance': 'inductance', 'id': request.form['circuit_id']})

# ---------------------------------------------------------------------------------------

            Newtotal_current_ct = Circuit.detail_circuit_and_loads_by_id({'circuit_id': request.form['circuit_id']})
            data2 = {}
            data2['circuit_id'] = request.form['circuit_id']
            data = {
                'method':circuit[0]['method'],
                'total_current': Newtotal_current_ct[0]['total_current_ct']
            }
            vp = round((0.018 * float(Newtotal_current_ct[0]['total_current_ct']) * float(Newtotal_current_ct[0]['total_length_ct']))/float(Newtotal_current_ct[0]['secctionmm2']),2)                                                          
            if vp < 4.5:
                current_by_method2 = Proyect.current_tri(data)
                data2['breakers'] = current_by_method2[0]['disyuntor']
                data2['elect_differencial'] = current_by_method2[0]['diferencial']
                data2['secctionmm2'] = current_by_method2[0]['secction_mm2']
                data2['current_by_method'] = current_by_method2[0][data['method']]
                Circuit.update_method(data2)
                Circuit.update_secctionmm2(data2)
                Circuit.update_breakers(data2)
                Circuit.update_elect_differencial(data2)
                data3 = { 'vp':round((0.018*float(request.form['total_length_ct'])*float(Newtotal_current_ct[0]['total_current_ct']))/float(data2['secctionmm2']),2), 'circuit_id':request.form['circuit_id']}
                Circuit.update_vp(data3)
                Circuit.updated_loads({'circuit_id': request.form['circuit_id']})
                if data['method'] == 'd1' or data['method'] == 'd2':
                    conduit = Circuit.conduit_tri_subte({'secctionmm2':data2['secctionmm2']})
                    data5 = {'conduit': conduit[0]['c5'], 'circuit_id':request.form['circuit_id']}
                    Circuit.update_conduit(data5)
                    return redirect('/loadbox/')
                else:
                    conduit = Circuit.conduit_tri_normal({'secctionmm2':data2['secctionmm2']})
                    data5 = {'conduit': conduit[0]['c5'], 'circuit_id':request.form['circuit_id']}
                    Circuit.update_conduit(data5)
                print('funciona por fin 380/220')
                return redirect('/loadbox/')
            else: 
                allcurrent_by_method = Circuit.vp_real(data)
                for all_current in allcurrent_by_method:
                    print(all_current)
                    if float(0.018 * float(Newtotal_current_ct[0]['total_current_ct']) * float(Newtotal_current_ct[0]['total_length_ct']))/float((all_current['secction_mm2'])) < 4.5:
                        data2['secctionmm2'] = all_current['secction_mm2']
                        data2['current_by_method'] = all_current['method']
                        break
                                                                
                current_by_method2 = Proyect.current_tri(data)
                data2['breakers'] = current_by_method2[0]['disyuntor']
                data2['elect_differencial'] = current_by_method2[0]['diferencial']
                Circuit.update_method(data2)
                Circuit.update_secctionmm2(data2)
                Circuit.update_breakers(data2)
                Circuit.update_elect_differencial(data2)
                data3 = { 'vp':round((0.018*float(Newtotal_current_ct[0]['total_length_ct'])*float(Newtotal_current_ct[0]['total_current_ct']))/float(data2['secctionmm2']),2), 'circuit_id':request.form['circuit_id']}
                Circuit.update_vp(data3)
                Circuit.updated_loads({'circuit_id': request.form['circuit_id']})
                if data['method'] == 'd1' or data['method'] == 'd2':
                    conduit = Circuit.conduit_tri_subte({'secctionmm2':data2['secctionmm2']})
                    data5 = {'conduit': conduit[0]['c5'], 'circuit_id':request.form['circuit_id']}
                    Circuit.update_conduit(data5)
                    return redirect('/loadbox/')
                else:
                    conduit = Circuit.conduit_tri_normal({'secctionmm2':data2['secctionmm2']})
                    data5 = {'conduit': conduit[0]['c5'], 'circuit_id':request.form['circuit_id']}
                    Circuit.update_conduit(data5)
                print('funciona por fin 380/220')
                return redirect('/loadbox/')

# ------- 380/380--------
        else:

            load['fp'] = request.form["fp3"]
            total_active_power = round((int(load['qty']) * float(load['active_power']))/1000,2)
            load['total_active_power'] = total_active_power
            load['total_apparent_power'] = round((total_active_power) / float(load['fp']),2)

            if load['impedance'] == "capacitance":
                load['total_reactive_power'] = round(-1 * ((load['total_apparent_power']) * math.sqrt(1 - float(load['fp'])**2)),2)
            
            else:
                load['total_reactive_power'] = round((load['total_apparent_power']) * math.sqrt(1 - float(load['fp'])**2),2)

            total_current = round(total_active_power/(math.sqrt(3) * float(float(voltage)) * float(load['fp'])),2)
            load['total_current'] = total_current
            Load.save(load)
            Circuit.updated_loads({'circuit_id': request.form['circuit_id']})

# ---------------------- CALCULO IMPEDANCIA Y FP ----------------------------------------

            new_total_fp = Circuit.new_total_fp({'id': request.form['circuit_id']})
            print(f" el valor de total_fp es {new_total_fp[0]['power_factor']}")
            Circuit.update_total_fp({'id': request.form['circuit_id'], 'new_total_fp':new_total_fp[0]['power_factor']})
            all_impedance = Load.all_impedance({'circuit_id': request.form['circuit_id']})
            count_cap = 0
            count_ind = 0
            for uu in all_impedance:
                if uu["impedance"] == "capacitance":
                    count_cap += 1
                else:
                    count_ind += 1

            if count_cap >= count_ind:
                if new_total_fp[0]['power_factor'] >= 0.95:
                    if load['total_reactive_power'] < 0:
                        print("no hay multa cap 1")
                    else:
                        print("no hay multa cap 2")
                elif 0.95 > new_total_fp[0]['power_factor'] >= 0.93:
                    if load['total_reactive_power'] > 0:
                        print("hay multa cap 1")
                    else:
                        print("hay multa cap revisar armonicos 2")
                Circuit.update_name_impedance({'name_impedance': 'capacitance', 'id': request.form['circuit_id']})
            else:
                if new_total_fp[0]['power_factor'] >= 0.93:
                    if load['total_reactive_power'] < 0:
                        print("hay multa cap 3")
                    else:
                        print("no hay multa cap aun que hay mas ind")
                    Circuit.update_name_impedance({'name_impedance': 'capacitance', 'id': request.form['circuit_id']})
                else:
                    print("hay multa cap revisar armonicos 2")
                    Circuit.update_name_impedance({'name_impedance': 'inductance', 'id': request.form['circuit_id']})
# ---------------------------------------------------------------------------------------

            Newtotal_current_ct = Circuit.detail_circuit_and_loads_by_id({'circuit_id': request.form['circuit_id']})
            data2 = {}
            data2['circuit_id'] = request.form['circuit_id']
            data = {
                'method':circuit[0]['method'],
                'total_current': Newtotal_current_ct[0]['total_current_ct']
            }
            vp = round((0.018 * float(Newtotal_current_ct[0]['total_current_ct']) * float(Newtotal_current_ct[0]['total_length_ct']))/float(Newtotal_current_ct[0]['secctionmm2']),2)                                                          
            if vp < 4.5:
                current_by_method2 = Proyect.current_tri(data)
                data2['breakers'] = current_by_method2[0]['disyuntor']
                data2['elect_differencial'] = current_by_method2[0]['diferencial']
                data2['secctionmm2'] = current_by_method2[0]['secction_mm2']
                data2['current_by_method'] = current_by_method2[0][data['method']]
                Circuit.update_method(data2)
                Circuit.update_secctionmm2(data2)
                Circuit.update_breakers(data2)
                Circuit.update_elect_differencial(data2)
                data3 = { 'vp':round((0.018*float(request.form['total_length_ct'])*float(Newtotal_current_ct[0]['total_current_ct']))/float(data2['secctionmm2']),2), 'circuit_id':request.form['circuit_id']}
                Circuit.update_vp(data3)
                Circuit.updated_loads({'circuit_id': request.form['circuit_id']})
                if data['method'] == 'd1' or data['method'] == 'd2':
                    conduit = Circuit.conduit_tri_subte({'secctionmm2':data2['secctionmm2']})
                    data5 = {'conduit': conduit[0]['c5'], 'circuit_id':request.form['circuit_id']}
                    Circuit.update_conduit(data5)
                    return redirect('/loadbox/')
                else:
                    conduit = Circuit.conduit_tri_normal({'secctionmm2':data2['secctionmm2']})
                    data5 = {'conduit': conduit[0]['c5'], 'circuit_id':request.form['circuit_id']}
                    Circuit.update_conduit(data5)
                print('funciona por fin 380/380')
                return redirect('/loadbox/')
            else: 
                allcurrent_by_method = Circuit.vp_real(data)
                for all_current in allcurrent_by_method:
                    print(all_current)
                    if float(0.018 * float(Newtotal_current_ct[0]['total_current_ct']) * float(Newtotal_current_ct[0]['total_length_ct']))/float((all_current['secction_mm2'])) < 4.5:
                        data2['secctionmm2'] = all_current['secction_mm2']
                        data2['current_by_method'] = all_current['method']
                        break
                                                                
                current_by_method2 = Proyect.current_tri(data)
                data2['breakers'] = current_by_method2[0]['disyuntor']
                data2['elect_differencial'] = current_by_method2[0]['diferencial']
                Circuit.update_method(data2)
                Circuit.update_secctionmm2(data2)
                Circuit.update_breakers(data2)
                Circuit.update_elect_differencial(data2)
                data3 = { 'vp':round((0.018*float(Newtotal_current_ct[0]['total_length_ct'])*float(Newtotal_current_ct[0]['total_current_ct']))/float(data2['secctionmm2']),2), 'circuit_id':request.form['circuit_id']}
                Circuit.update_vp(data3)
                Circuit.updated_loads({'circuit_id': request.form['circuit_id']})
                if data['method'] == 'd1' or data['method'] == 'd2':
                    conduit = Circuit.conduit_tri_subte({'secctionmm2':data2['secctionmm2']})
                    data5 = {'conduit': conduit[0]['c5'], 'circuit_id':request.form['circuit_id']}
                    Circuit.update_conduit(data5)
                    return redirect('/loadbox/')
                else:
                    conduit = Circuit.conduit_tri_normal({'secctionmm2':data2['secctionmm2']})
                    data5 = {'conduit': conduit[0]['c5'], 'circuit_id':request.form['circuit_id']}
                    Circuit.update_conduit(data5)
                print('funciona por fin 380/380')
                return redirect('/loadbox/')


# --------------------- FROM AJAX ABOUT EDIT AND DELETE CIRCUITS BY TDS AND TGS -----------------------------------------------------------


@app.route('/api/delete/load', methods=["POST"])
def delete_load():
    Load.delete({'load_id':request.form['load']})
    print('borrado')
    Circuit.updated_loads({'circuit_id':request.form['circuit']})
    totalCircuit = Circuit.detail_circuit_by_id({'circuit_id':request.form['circuit']})
    print(totalCircuit[0]['total_center'])

    if totalCircuit != 0 and totalCircuit[0]['total_center']:

# ---------------------- CALCULO IMPEDANCIA Y FP ----------------------------------------
        new_total_fp = Circuit.new_total_fp({'id': request.form['circuit']})
        print(f" el valor de total_fp es {new_total_fp[0]['power_factor']}")
        Circuit.update_total_fp({'id': request.form['circuit'], 'new_total_fp':new_total_fp[0]['power_factor']})
# ---------------------------------------------------------------------------------------

        circuitv2 = Circuit.detail_circuit_and_loads_by_id({'circuit_id':request.form['circuit']})
        if float(circuitv2[0]['single_voltage']) == 0.220:
            data2 = {}
            data2['circuit_id'] = request.form['circuit']
            data = {
                'method': circuitv2[0]['method'],
                'total_current': circuitv2[0]['total_current_ct']
            }                                                              
            allcurrent_by_method = Circuit.vp_real(data)
            for all_current in allcurrent_by_method:
                if float(2 * 0.018 * float(circuitv2[0]['total_current_ct']) * float(circuitv2[0]['total_length_ct']))/float((all_current['secction_mm2'])) < 4.5:
                    data2['secctionmm2'] = all_current['secction_mm2']
                    data2['current_by_method'] = all_current['method']
                    break
                                                                    
            current_by_method2 = Proyect.current(data)
            data2['breakers'] = current_by_method2[0]['disyuntor']
            data2['elect_differencial'] = current_by_method2[0]['diferencial']
            Circuit.update_method(data2)
            Circuit.update_secctionmm2(data2)
            Circuit.update_breakers(data2)
            Circuit.update_elect_differencial(data2)
            data3 = { 'vp':round((2*0.018*float(circuitv2[0]['total_length_ct'])*float(circuitv2[0]['total_current_ct']))/float(data2['secctionmm2']),2), 'circuit_id': request.form['circuit']}
            Circuit.update_vp(data3)
            Circuit.updated_loads({'circuit_id': request.form['circuit']})
            if circuitv2[0]['method'] == 'd1' or circuitv2[0]['method'] == 'd2':
                conduit = Circuit.conduit_mono_subte({'secctionmm2':data2['secctionmm2']})
                data5 = {'conduit': conduit[0]['c3'], 'circuit_id': request.form['circuit']}
                Circuit.update_conduit(data5)
            else:
                conduit = Circuit.conduit_mono_normal({'secctionmm2':data2['secctionmm2']})
                data5 = {'conduit': conduit[0]['c3'], 'circuit_id': request.form['circuit']}
                Circuit.update_conduit(data5)
            print('funciona por fin 220')
            return redirect('/loadbox/')
        
        # -------- trifasico ----------
        else:
            data2 = {}
            data2['circuit_id'] = request.form['circuit']
            data = {
                'method': circuitv2[0]['method'],
                'total_current': circuitv2[0]['total_current_ct']
            }                                                          
            allcurrent_by_method = Circuit.vp_real(data)
            for all_current in allcurrent_by_method:
                if float(0.018 * float(circuitv2[0]['total_current_ct']) * float(circuitv2[0]['total_length_ct']))/float((all_current['secction_mm2'])) < 4.5:
                    data2['secctionmm2'] = all_current['secction_mm2']
                    data2['current_by_method'] = all_current['method']
                    break
                                                            
            current_by_method2 = Proyect.current_tri(data)
            data2['breakers'] = current_by_method2[0]['disyuntor']
            data2['elect_differencial'] = current_by_method2[0]['diferencial']
            Circuit.update_method(data2)
            Circuit.update_secctionmm2(data2)
            Circuit.update_breakers(data2)
            Circuit.update_elect_differencial(data2)
            data3 = { 'vp':round((0.018*float(circuitv2[0]['total_length_ct'])*float(circuitv2[0]['total_current_ct']))/float(data2['secctionmm2']),2), 'circuit_id':request.form['circuit']}
            Circuit.update_vp(data3)
            Circuit.updated_loads({'circuit_id': request.form['circuit']})
            if circuitv2[0]['method'] == 'd1' or circuitv2[0]['method'] == 'd2':
                conduit = Circuit.conduit_tri_subte({'secctionmm2':data2['secctionmm2']})
                data5 = {'conduit': conduit[0]['c5'], 'circuit_id':request.form['circuit']}
                Circuit.update_conduit(data5)
            else:
                conduit = Circuit.conduit_tri_normal({'secctionmm2':data2['secctionmm2']})
                data5 = {'conduit': conduit[0]['c5'], 'circuit_id':request.form['circuit']}
                Circuit.update_conduit(data5)
            print('funciona por fin 380')
            return redirect('/loadbox/')
    else:
        Circuit.delete_circuit_by_id({'circuit_id': request.form['circuit']})


@app.route('/api/delete/circuit', methods=['POST'])
def delete_circuit():
    Load.delete_load_by_circuit_id({'circuit_id': request.form['circuitv2']})
    Circuit.delete_circuit_by_id({'circuit_id': request.form['circuitv2']})
    return redirect('/loadbox/')

@app.route('/api/delete/tgs', methods=['POST'])
def delete_tgs():
    Tgs.delete_load_by_tgId({'tg_id':request.form['tgs_delete']})
    Tgs.delete_circuits_by_tgId({'tg_id':request.form['tgs_delete']})
    Tgs.delete_total_tgs_by_tgId({'tab_secondary':request.form['tgs_delete']})
    Tgs.delete_tds_by_tgId({'tg_id':request.form['tgs_delete']})
    Tgs.delete_tgs_by_tgId({'id':request.form['tgs_delete']})
    return redirect('/loadbox/')

@app.route('/api/delete/tds', methods=['POST'])
def delete_tds():
    Tds.delete_load_by_tdId({'td_id':request.form['tds_delete']})
    Tds.delete_circuits_by_tdId({'td_id':request.form['tds_delete']})
    Tds.delete_total_tds_by_tdId({'td_id':request.form['tds_delete']})
    Tds.delete_tds_by_tdId({'id':request.form['tds_delete']})
    return redirect('/loadbox/')

@app.route('/api/delete/proyect', methods=['POST'])
def delete_pro():
    allpro = Proyect.get_all_tgs_by_proyect_id({'id':request.form['proyect_id']})
    if len(allpro) > 0:
        return jsonify(data=allpro, success=False)
    else:
        Proyect.delete_proyect_by_proyec_id({'id':request.form['proyect_id']})
        return jsonify(success=True)



# -------------------------------------------------------------------------------------------------------------------
# ------------------------------------SUMMARY PROYECTS --------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------


@app.route('/api/excel_tds/<int:td_id>')
def tds_to_excel(td_id):
    data_list = Tds.detail_to_excel({'td_id': td_id})
    name_td = Tds.get_td_by_id({'id':td_id})
    if data_list:
        df = pd.DataFrame(data_list)
        buffer = io.BytesIO()
        df.to_excel(buffer, index=False, startrow=3, startcol=3)
        response = make_response(buffer.getvalue())
        response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        response.headers['Content-Disposition'] = 'attachment; filename=Cuadro_de_cargas_'+ str(name_td[0]['name'])+'.xlsx'
        return response
    else:
        return "No hay circuitos, tablero de distribucíon vacío."



@app.route('/api/excel_tgs/<int:tg_id>')
def tgs_to_excel(tg_id):
    data_list = Tgs.detail_to_excel({'tg_id': tg_id})
    name_tg = Tgs.name_tg({'tg_id': tg_id})
    data =[]
    if data_list:
        for tg in data_list:
            if tg['Cantidad'] != None:
                data.append(tg)
        df = pd.DataFrame(data)
        buffer = io.BytesIO()
        df.to_excel(buffer, index=False, startrow=3, startcol=3)
        response = make_response(buffer.getvalue())
        response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        response.headers['Content-Disposition'] = 'attachment; filename=Cuadro_de_cargas_' + str(name_tg[0]['name']) +'.xlsx'
        return response
    else:
        return "No hay circuitos, tablero general vacío."

@app.route('/api/summary-tds/', methods=["POST"])
def allcircuits_tds():
    detail = Tds.summary_circuits_tds({'td_id': request.form['id']})
    print(detail)
    return jsonify(detail)


@app.route("/api/edit_tgs_name/", methods=["POST"])
def edit_tgs_name():
    tgsid = {
        'id': request.form['id'],
        'name': "Tablero " + request.form['name'],
        'tag': request.form['tag']
    }
    Tgs.edit_name(tgsid)   
    print(tgsid)
    return redirect('/loadbox')


@app.route("/api/edit_tds_name/", methods=["POST"])
def edit_tds_name():
    tdsid = {
        'id': request.form['id'],
        'name': "Tablero " + request.form['name'],
        'tag': request.form['tag']
    }
    Tds.edit_name(tdsid)
    Total_tds.edit_name_total({'ref': tdsid['name'], 'td_id':tdsid['id']})
    print(tdsid)
    return redirect('/loadbox')