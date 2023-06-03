from flask import render_template,redirect,session,request, flash, jsonify, url_for
from src import app
from src.models.user import User
from src.models.proyects import Proyect
from src.models.tgs import Tgs
from src.models.circuits import Circuit
from src.models.loads import Load
from src.models.tds import Tds

from flask_bcrypt import Bcrypt
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
    return render_template('house.html', user=user, proyects=proyects, tgs=tgs, wires=wires)



#  -------------------------------------------------NEW PROYECTS ---------------------------------------------------



@app.route('/new_proyect', methods=['POST'])
def new_proyect():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'name': request.form['name'],
        'user_id': session['user_id']
    }

    Proyect.save(data)
    return redirect('/loadbox')



# ------------------------------------------------ADD NEW GENERAL TABLE-------------------------------------------------



@app.route('/add_tgs', methods=['POST'])
def add_tgs():
    if 'user_id' not in session:
        return redirect('/logout')
    
    data = {
        'name': request.form['name'],
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
        'name': request.form['name'],
        'tag': request.form['tag'],
        'tg_id': request.form['tg_id']
    }
    print(data)
    Tds.add_tds(data)
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
        data = {
            'name': request.form['name'],
            'nameloads': request.form['nameloads'],
            'ref': request.form['ref'],
            'method': request.form['method'],
            'single_voltage': request.form['single_voltage'],
            'total_length_ct': request.form['total_length_ct'],
            'tg_id' : request.form['tg_id']
        }
        td_id = request.form.get('td_id')
        if td_id and td_id.isdigit():
            data['td_id'] = request.form['td_id']
        else:
            data['td_id'] = None

        data['wires'] = request.form['type_isolation']
        data['type_circuit'] = request.form['type_circuit']
        circuit_id = Circuit.add_circuit(data)
        data['qty'] = request.form['qty']
        data['power'] = request.form['power']
        total_power = round((int(data['qty']) * float(data['power']))/1000,2)
        total_current = round(total_power/float(request.form['single_voltage']),2)
        print(total_current)
        data1 = {'method':data['method'],'total_current':total_current}
        current_by_method= Proyect.current(data1)
        print(current_by_method)
        vp = (2 * 0.018 * float(total_current) * float(data['total_length_ct']))/float(current_by_method[0]['secction_mm2'])
        print(vp)
        data2 = {}
        data2['circuit_id'] = circuit_id
        if vp < 4.5:                                                            
            current_by_method2 = Proyect.current(data1)
            print(current_by_method2)
            data2['breakers'] = current_by_method2[0]['disyuntor']
            data2['elect_differencial'] = current_by_method2[0]['diferencial']
            data2['secctionmm2'] = current_by_method2[0]['secction_mm2']
            data2['current_by_method'] = current_by_method2[0][data['method']]
            print(data2)
            Circuit.update_method(data2)
            Circuit.update_secctionmm2(data2)
            Circuit.update_breakers(data2)
            Circuit.update_elect_differencial(data2)
            data3 = { 'vp':round((2*0.018*float(data['total_length_ct'])*float(total_current))/float(data2['secctionmm2']),2), 'circuit_id':circuit_id}
            print(data3)
            Circuit.update_vp(data3)
            data4 = {'nameloads':data['nameloads'],'qty': data['qty'], 'power':data['power'], 'total_power':total_power, 'fp':float(1.00),'length': request.form['total_length_ct'], 'total_current': total_current,'circuit_id': circuit_id}
            Load.save(data4)
            Circuit.updated_loads({'circuit_id':circuit_id})
            print('funciona por fin 220')
            return redirect('/loadbox')

        else: 
            allcurrent_by_method = Circuit.vp_real(data1)
            for all_current in allcurrent_by_method:
                print(all_current)
                if float(2 * 0.018 * float(total_current) * float(data['total_length_ct']))/float((all_current['secction_mm2'])) < 4.5:
                    data2['secctionmm2'] = all_current['secction_mm2']
                    data2['current_by_method'] = all_current['method']
                    break
            print(data2)
            print(data1)                                                             
            current_by_method2 = Proyect.current(data1)
            print(current_by_method2)
            data2['breakers'] = current_by_method2[0]['disyuntor']
            data2['elect_differencial'] = current_by_method2[0]['diferencial']
            print(data2)
            Circuit.update_method(data2)
            Circuit.update_secctionmm2(data2)
            Circuit.update_breakers(data2)
            Circuit.update_elect_differencial(data2)
            data3 = { 'vp':round((2*0.018*float(data['total_length_ct'])*float(total_current))/float(data2['secctionmm2']),2), 'circuit_id':circuit_id}
            print(data3)
            Circuit.update_vp(data3)
            data4 = {'nameloads':data['nameloads'],'qty': data['qty'], 'power':data['power'], 'total_power':total_power, 'fp':float(1.00),'length': request.form['total_length_ct'], 'total_current': total_current,'circuit_id': circuit_id}
            Load.save(data4)
            Circuit.updated_loads({'circuit_id':circuit_id})
            print('funciona por fin 220')
            return redirect('/loadbox')


# ------------------ CALCULOS TRIFASICOS --------------------
    else:
        data = {
            'name': request.form['name'],
            'nameloads': request.form['nameloads'],
            'ref': request.form['ref'],
            'method': request.form['method'],
            'single_voltage': request.form['single_voltage'],
            'total_length_ct': request.form['total_length_ct'],
            'tg_id' : request.form['tg_id']
        }
        td_id = request.form.get('td_id')
        if td_id and td_id.isdigit():
            data['td_id'] = request.form['td_id']
        else:
            data['td_id'] = None

        data['wires'] = request.form['type_isolation']
        data['type_circuit'] = request.form['type_circuit']
        circuit_id = Circuit.add_circuit(data)
        data['qty'] = request.form['qty']
        data['power'] = request.form['power']
        total_power = round((int(data['qty']) * float(data['power']))/1000,2)
        print(total_power)
        total_current = round(total_power/(float(request.form['single_voltage']) * float(1.7320508076) * float(request.form['fp'])),2)
        print(total_current)
        data1 = {'method':data['method'],'total_current':total_current}
        current_by_method= Proyect.current_tri(data1)
        print(current_by_method[0]['secction_mm2'])
        vp = (0.018 * float(total_current) * float(data['total_length_ct']))/float(current_by_method[0]['secction_mm2'])
        data2 = {}
        data2['circuit_id'] = circuit_id
        print(round(vp,2))                                                    
        if vp < 4.5:
            current_by_method2 = Proyect.current_tri(data1)
            print(current_by_method2)
            data2['secctionmm2'] = current_by_method2[0]['secction_mm2']
            data2['current_by_method'] = current_by_method2[0][data['method']]
            data2['breakers'] = current_by_method2[0]['disyuntor']
            data2['elect_differencial'] = current_by_method2[0]['diferencial']
            print(data2)
            Circuit.update_method(data2)
            Circuit.update_secctionmm2(data2)
            Circuit.update_breakers(data2)
            Circuit.update_elect_differencial(data2)
            data3 = { 'vp':round((0.018*float(data['total_length_ct'])*float(total_current))/float(data2['secctionmm2']),2), 'circuit_id':circuit_id}
            print(data3)
            Circuit.update_vp(data3)
            data4 = {'nameloads':data['nameloads'],'qty': data['qty'], 'power':data['power'], 'total_power':total_power, 'fp':request.form['fp'],'length': request.form['total_length_ct'] ,'total_current': total_current,'circuit_id': circuit_id}
            Load.save(data4)
            Circuit.updated_loads({'circuit_id':circuit_id})
            print('funciona por fin 380')
            return redirect('/loadbox')
        else: 
            allcurrent_by_method = Circuit.vp_real(data1)
            for all_current in allcurrent_by_method:
                print(all_current)
                if float(0.018 *float(total_current) * float(data['total_length_ct']))/float((all_current['secction_mm2'])) < 4.5:
                    data2['current_by_method'] =  all_current['method']
                    data2['secctionmm2'] = all_current['secction_mm2']
                    break
                                                          
            current_by_method2 = Proyect.current_tri(data1)
            print(current_by_method2)
            data2['current_by_method'] = current_by_method2[0][data['method']]
            data2['breakers'] = current_by_method2[0]['disyuntor']
            data2['elect_differencial'] = current_by_method2[0]['diferencial']
            print(data2)
            Circuit.update_method(data2)
            Circuit.update_secctionmm2(data2)
            Circuit.update_breakers(data2)
            Circuit.update_elect_differencial(data2)
            data3 = { 'vp':round((0.018*float(data['total_length_ct'])*float(total_current))/float(data2['secctionmm2']),2), 'circuit_id':circuit_id}
            print(data3)
            Circuit.update_vp(data3)
            data4 = {'nameloads':data['nameloads'],'qty': data['qty'], 'power':data['power'], 'total_power':total_power, 'fp':request.form['fp'],'length': request.form['total_length_ct'] ,'total_current': total_current,'circuit_id': circuit_id}
            Load.save(data4)
            Circuit.updated_loads({'circuit_id':circuit_id})
            print('funciona por fin 380')
            return redirect('/loadbox')



# ---------------------------------------------- AJAX ID CIRCUITS----------------------------------------------------------------


@app.route('/api/tgs', methods=['POST'])
def get_tgs():
    proyect = request.form['proyect']
    tgs1 = Tgs.get_tgs_by_project({'proyect_id': proyect})
    return jsonify(tgs1)

@app.route('/api/tds', methods=['POST'])
def get_tds():
    tg_id = request.form['tgs']
    circuit_tg = Circuit.get_all_circuits_by_tg_id({'tg_id':tg_id})
    tgs = Tds.get_all_tds_by_tg_id({'tg_id':tg_id})
    return jsonify(tgs, circuit_tg)


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
        print(circuit_td)
    else:
        pass
    return jsonify(circuit_td)

# --------------------- FROM AJAX ABOUT DETAIL CIRCUITS BY TDS AND TGS -----------------------------------------------------------

@app.route('/api/detail', methods=['POST'])
def detai_circuit_tds():
    circuit_id = request.form['circuit']
    circuitos = Circuit.detail_circuit_and_loads_by_id({'circuit_id': circuit_id})
    print(circuitos)
    return jsonify(circuitos)


@app.route('/add_load', methods=['POST'])
def add_loads():
    circuit = Circuit.detail_circuit_and_loads_by_id({'circuit_id': request.form['circuit_id']})

# ------- ADD LOADS IN CIRCUITS MONOPHASE -----------------

    if float(circuit[0]['single_voltage']) == 0.220:
        print(circuit[0]['total_current_ct'])
        load = {
            'nameloads': request.form['nameloads'],
            'qty': request.form['qty'],
            'circuit_id': request.form['circuit_id'],
            'power': request.form['power'],
            'fp': request.form['fp'],
            'length': request.form['total_length_ct']
        }
        total_power = round(float((load['qty'])) * float(load['power'])/1000,2)
        total_current = round(total_power/float(circuit[0]['single_voltage']),2)
        load['total_current'] = total_current
        load['total_power'] = total_power
        print(load)
        Load.save(load)
        Circuit.updated_loads({'circuit_id': request.form['circuit_id']})
        Newtotal_current_ct = Circuit.detail_circuit_and_loads_by_id({'circuit_id': request.form['circuit_id']})
        print(Newtotal_current_ct[0]['total_current_ct'])

        data = {
            'method':circuit[0]['method'],
            'total_current': Newtotal_current_ct[0]['total_current_ct']
        }
        vp = round((2 * 0.018 * float(Newtotal_current_ct[0]['total_current_ct']) * float(request.form['total_length_ct']))/float(Newtotal_current_ct[0]['secctionmm2']),2)
        data2 = {}
        data2['circuit_id'] = request.form['circuit_id']
        print(vp)                                                              
        if vp < 4.5:
            current_by_method2 = Proyect.current(data)
            data2['breakers'] = current_by_method2[0]['disyuntor']
            data2['elect_differencial'] = current_by_method2[0]['diferencial']
            data2['secctionmm2'] = current_by_method2[0]['secction_mm2']
            data2['current_by_method'] = current_by_method2[0][data['method']]
            print(data2)
            Circuit.update_method(data2)
            Circuit.update_secctionmm2(data2)
            Circuit.update_breakers(data2)
            Circuit.update_elect_differencial(data2)
            data3 = { 'vp':round((2*0.018*float(request.form['total_length_ct'])*float(Newtotal_current_ct[0]['total_current_ct']))/float(data2['secctionmm2']),2), 'circuit_id':request.form['circuit_id']}
            print(data3)
            Circuit.update_vp(data3)
            Circuit.updated_loads({'circuit_id': request.form['circuit_id']})
            print('funciona por fin 220')
            return redirect('/loadbox')
        else: 
            allcurrent_by_method = Circuit.vp_real(data)
            for all_current in allcurrent_by_method:
                print(all_current)
                if float(2 * 0.018 * float(Newtotal_current_ct[0]['total_current_ct']) * float(request.form['total_length_ct']))/float((all_current['secction_mm2'])) < 4.5:
                    data2['secctionmm2'] = all_current['secction_mm2']
                    data2['current_by_method'] = all_current['method']
                    break
                                                             
        current_by_method2 = Proyect.current(data)
        print(current_by_method2)
        data2['breakers'] = current_by_method2[0]['disyuntor']
        data2['elect_differencial'] = current_by_method2[0]['diferencial']
        print(data2)
        Circuit.update_method(data2)
        Circuit.update_secctionmm2(data2)
        Circuit.update_breakers(data2)
        Circuit.update_elect_differencial(data2)
        data3 = { 'vp':round((2*0.018*float(request.form['total_length_ct'])*float(Newtotal_current_ct[0]['total_current_ct']))/float(data2['secctionmm2']),2), 'circuit_id':request.form['circuit_id']}
        print(data3)
        Circuit.update_vp(data3)
        Circuit.updated_loads({'circuit_id': request.form['circuit_id']})
        print('funciona por fin 220')
        return redirect('/loadbox')

# ------- ADD LOADS IN CIRCUITS TRIPHASE -----------------
    else:
        print("aca estamos")
        print(circuit[0]['single_voltage'])
        load = {
        'nameloads': request.form['nameloads'],
        'qty': request.form['qty'],
        'circuit_id': request.form['circuit_id'],
        'power': request.form['power'],
        'fp': request.form['fp'],
        'length': request.form['total_length_ct']
        }
        print(load)
        total_power = round(float((load['qty'])) * float(load['power'])/1000,2)
        total_current = round(total_power/(float(1.7320508076) * float(circuit[0]['single_voltage']) * float(load['fp'])),2)
        load['total_current'] = total_current
        load['total_power'] = total_power
        print(load)
        Load.save(load)
        Circuit.updated_loads({'circuit_id': request.form['circuit_id']})
        Newtotal_current_ct = Circuit.detail_circuit_and_loads_by_id({'circuit_id': request.form['circuit_id']})
        print(Newtotal_current_ct[0]['total_current_ct'])
        data2 = {}
        data2['circuit_id'] = request.form['circuit_id']
        data = {
            'method':circuit[0]['method'],
            'total_current': Newtotal_current_ct[0]['total_current_ct']
        }
        vp = round((0.018 * float(Newtotal_current_ct[0]['total_current_ct']) * float(request.form['total_length_ct']))/float(Newtotal_current_ct[0]['secctionmm2']),2)
        print(vp)                                                              
        if vp < 4.5:
            current_by_method2 = Proyect.current_tri(data)
            print(current_by_method2)
            data2['breakers'] = current_by_method2[0]['disyuntor']
            data2['elect_differencial'] = current_by_method2[0]['diferencial']
            data2['secctionmm2'] = current_by_method2[0]['secction_mm2']
            data2['current_by_method'] = current_by_method2[0][data['method']]
            print(data2)
            Circuit.update_method(data2)
            Circuit.update_secctionmm2(data2)
            Circuit.update_breakers(data2)
            Circuit.update_elect_differencial(data2)
            data3 = { 'vp':round((0.018*float(request.form['total_length_ct'])*float(Newtotal_current_ct[0]['total_current_ct']))/float(data2['secctionmm2']),2), 'circuit_id':request.form['circuit_id']}
            print(data3)
            Circuit.update_vp(data3)
            Circuit.updated_loads({'circuit_id': request.form['circuit_id']})
            print('funciona por fin 380')
            return redirect('/loadbox/')
        else: 
            allcurrent_by_method = Circuit.vp_real(data)
            for all_current in allcurrent_by_method:
                print(all_current)
                if float(0.018 * float(Newtotal_current_ct[0]['total_current_ct']) * float(request.form['total_length_ct']))/float((all_current['secction_mm2'])) < 4.5:
                    data2['secctionmm2'] = all_current['secction_mm2']
                    data2['current_by_method'] = all_current['method']
                    break
                                                             
            current_by_method2 = Proyect.current_tri(data)
            print(current_by_method2)
            data2['breakers'] = current_by_method2[0]['disyuntor']
            data2['elect_differencial'] = current_by_method2[0]['diferencial']
            print(data2)
            Circuit.update_method(data2)
            Circuit.update_secctionmm2(data2)
            Circuit.update_breakers(data2)
            Circuit.update_elect_differencial(data2)
            data3 = { 'vp':round((0.018*float(request.form['total_length_ct'])*float(Newtotal_current_ct[0]['total_current_ct']))/float(data2['secctionmm2']),2), 'circuit_id':request.form['circuit_id']}
            print(data3)
            Circuit.update_vp(data3)
            Circuit.updated_loads({'circuit_id': request.form['circuit_id']})
            print('funciona por fin 380')
            return redirect('/loadbox/')


# --------------------- FROM AJAX ABOUT EDIT AND DELETE CIRCUITS BY TDS AND TGS -----------------------------------------------------------


@app.route('/api/delete/load', methods=["POST"])
def delete_load():
    Load.delete({'load_id':request.form['load']})
    print('borrado')
    Circuit.updated_loads({'circuit_id':request.form['circuit']})
    circuitv2 = Circuit.detail_circuit_and_loads_by_id({'circuit_id':request.form['circuit']})
    if float(circuitv2[0]['single_voltage']) == 0.220:
        vp = round((2 * 0.018 * float(circuitv2[0]['total_current_ct']) * float(circuitv2[0]['total_length_ct']))/float(circuitv2[0]['secctionmm2']),2)
        print(vp)
        data2 = {}
        data2['circuit_id'] = request.form['circuit']
        data = {
            'method': circuitv2[0]['method'],
            'total_current': circuitv2[0]['total_current_ct']
        }                                                              
        if vp < 4.5:
            current_by_method2 = Proyect.current(data)
            print(current_by_method2)
            data2['secctionmm2'] = current_by_method2[0]['secction_mm2']
            data2['circuit_id'] = request.form['circuit']
            data2['current_by_method'] = current_by_method2[0][data['method']]
            data2['breakers'] = current_by_method2[0]['disyuntor']
            data2['elect_differencial'] = current_by_method2[0]['diferencial']
            print(data2)
            Circuit.update_method(data2)
            Circuit.update_secctionmm2(data2)
            Circuit.update_breakers(data2)
            Circuit.update_elect_differencial(data2)
            data3 = { 'vp':round( vp ,2), 'circuit_id': request.form['circuit']}
            print(data3)
            Circuit.update_vp(data3)
            Circuit.updated_loads({'circuit_id': request.form['circuit']})
            print('funciona por fin 220')
            return redirect('/loadbox/')
        else: 
            allcurrent_by_method = Circuit.vp_real(data)
            for all_current in allcurrent_by_method:
                print(all_current)
                if float(2 * 0.018 * float(circuitv2[0]['total_current_ct']) * float(circuitv2[0]['total_length_ct']))/float((all_current['secction_mm2'])) < 4.5:
                    data2['secctionmm2'] = all_current['secction_mm2']
                    data2['current_by_method'] = all_current['method']
                    break
                                                                
            current_by_method2 = Proyect.current(data)
            print(current_by_method2)
            data2['breakers'] = current_by_method2[0]['disyuntor']
            data2['elect_differencial'] = current_by_method2[0]['diferencial']
            print(data2)
            Circuit.update_method(data2)
            Circuit.update_secctionmm2(data2)
            Circuit.update_breakers(data2)
            Circuit.update_elect_differencial(data2)
            data3 = { 'vp':round((2*0.018*float(circuitv2[0]['total_length_ct'])*float(circuitv2[0]['total_current_ct']))/float(data2['secctionmm2']),2), 'circuit_id': request.form['circuit']}
            print(data3)
            Circuit.update_vp(data3)
            Circuit.updated_loads({'circuit_id': request.form['circuit']})
            print('funciona por fin 220')
            return redirect('/loadbox/')
    else:
        print('trifasico')
        return redirect('/loadbox/')
    
@app.route('/api/delete/circuit', methods=['POST'])
def delete_circuit():
    print(request.form['circuitv2'])
    Load.delete_load_by_circuit_id({'circuit_id': request.form['circuitv2']})
    Circuit.delete_load_by_circuit_id({'circuit_id': request.form['circuitv2']})
    return redirect('/loadbox/')


# -------------------------------------------------------------------------------------------------------------------
# ------------------------------------SUMMARY PROYECTS --------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

@app.route('/summary')
def summary():
    if 'user_id' not in session:
        return redirect('/logout')

    data ={'id': session['user_id']}

    user = User.get_by_id(data)
    projects = Proyect.get_all_proyect_by_user_id(data)
    tgs = Proyect.get_all_tgs_by_user_id(data)
    return render_template('summary.html', user=user, projects=projects, tgs = tgs)



@app.route('/api/pro_id/')
def user_id():
    print(request.args.get('proyect_id'))
    tg = Tgs.get_tgs_by_project({'proyect_id': request.args.get('proyect_id')})
    return jsonify(tg)

@app.route('/api/tg_id')
def tg_id():
    td = Tds.get_all_tds_by_tg_id({'tg_id': request.args.get('tg_id')})
    print(td)
    return jsonify(td)

