from flask import render_template,redirect,session,request, flash
from src import app
from src.models.user import User
from src.models.proyects import Proyect

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/loadbox/')
def loadbox():
    if 'user_id' not in session:
        return redirect('/logout')

    data ={
        'id': session['user_id']
    }
    user = User.get_by_id(data)
    proyects = Proyect.get_all_proyect_by_user_id(data)
    # tds = Proyect.get_all_tds_by_proyect_id_and_user_id(data)
    return render_template('house.html', user=user, proyects=proyects)


@app.route('/new_circuit', methods=['POST'])
def new_circuits():

    if 'user_id' not in session:
        return redirect('/logout')
    
    if not Proyect.validate_circuit(request.form):
        return redirect('/loadbox')

    data = {
        'name': request.form['name'],
        'voltage': request.form['voltage'],
        'methods': request.form['methods'],
        'qty': request.form['qty'],
        'load': request.form['load'],
        'lenght': request.form['lenght'],
    }


    total_load = (int(data['qty']) * int(data['load']))/1000 
    total_current = round(total_load/float(data['voltage']),2)
    print(total_current)
    data1 = {'method':data['methods'],'total_current':int(total_current)}
    current_by_method= Proyect.current(data1)
    print(current_by_method)
    secc_min = round((2*0.018*float(data['lenght'])*total_current)/4.5, 2)
    print(secc_min)
    return redirect('/loadbox')



