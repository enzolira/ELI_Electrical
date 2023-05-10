from flask import render_template,redirect,session,request, flash, jsonify
from src import app
from src.models.user import User
from src.models.proyects import Proyect
from src.models.tgs import Tgs
from src.models.circuits import Circuit
from src.models.loads import Load

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


#  -----------MAIN PAGE --------------------

@app.route('/loadbox/')
def loadbox():
    if 'user_id' not in session:
        return redirect('/logout')

    data ={'id': session['user_id']}

    user = User.get_by_id(data)
    proyects = Proyect.get_all_proyect_by_user_id(data)
    tgs = Proyect.get_all_tgs_by_proyect_id_and_user_id(data)
    wires= Proyect.get_all_wires()
    circuits = Circuit.get_all_circuits_by_user_user_id(data)
    print(circuits)
    return render_template('house.html', user=user, proyects=proyects, tgs=tgs, wires=wires, circuits=circuits)

# -------------NEW PROYECT------------------

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

# ---------------ADD NEW GENERAL TABLE------------------

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

# ---------------ADD NEW DISTRIBUCION TABLE------------------

@app.route('/add_tds', methods=['POST'])
def add_tds():
    if 'user_id' not in session:
        return redirect('/logout')
    
    data = {
        'name': request.form['name'],
        'tag': request.form['tag'],
        'tg_id': request.form['tg_id']
    }

    Tgs.add_tgs(data)
    return redirect('/loadbox')

# -------------- CREATE CIRCUITS--------------------------

@app.route('/new_circuit', methods=['POST'])
def new_circuits():

    if 'user_id' not in session:
        return redirect('/logout')
    
    if not Proyect.validate_circuit(request.form):
        return redirect('/loadbox/')

    data = {
        'name': request.form['name'],
        'ref': request.form['ref'],
        'single_voltage': request.form['single_voltage'],
        'method': request.form['method'],
        'fp': request.form['fp'],
        'length': request.form['length'],
        'tg_id' : request.form['tg_id'],
        'wires' : request.form['type_isolation'],
        'type_circuit' : request.form['type_circuit']
    }
    circuit_id = Circuit.add_circuit(data)
    data['qty'] = request.form['qty']
    data['power'] = request.form['power']
    total_power = (int(data['qty']) * int(data['power']))/1000
    total_current = round(total_power/float(data['single_voltage']),2)
    data1 = {'method':data['method'],'total_current':total_current}
    current_by_method= Proyect.current(data1)
    secc_min = round((2*0.018*float(data['length'])*total_current)/4.5, 2)
    data2 = {}
    data2['secctionmm2'] = current_by_method[0]['secction_mm2']
    print(data2)
    # vp_real = round((2*0.018*float(data['length']*total_current))/data2[0]['secctionmm2'],2)
    # data['vp'] = vp_real
    data2['current_by_method'] = current_by_method[0][data['method']]
    circuit_id = Circuit.add_circuit(data)
    print(circuit_id)
    if circuit_id:
        data3 = {'qty': data['qty'], 'power':data['power'], 'single_voltage':data['single_voltage'],'circuit_id': circuit_id}
        Load.save(data3)
    else:
        pass
    # Aquí puedes tomar medidas en consecuencia si no se pudo agregar el circuito
    # print(data)
    # print(total_current)
    # print(secc_min)
    # print(current_by_method[0]['secction_mm2'])
    # print(data2)

    return redirect('/loadbox/')



# ------------ AJAX----------------------

@app.route('/api/tgs', methods=['POST'])
def get_tgs():
    proyect = request.form['proyect']
    tgs = Tgs.get_tgs_by_project({'proyect_id': proyect})
    return jsonify(tgs)



