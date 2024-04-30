from flask import render_template,redirect,session,request, flash, jsonify, url_for
from datetime import datetime
from src import app
from src.models.user import User
from src.models.proyects import Proyect
from src.models.planification import Jobs

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#  -------------------------------------------------MAIN PAGE ---------------------------------------------------

@app.route('/planning/')
def plan():
    if 'user_id' not in session:
        return redirect('/logout')

    data ={'id': session['user_id']}

    user = User.get_by_id(data)
    proyects = Proyect.get_all_proyect_by_user_id(data)
    # proyects = list(enumerate(proyects, 1))
    return render_template('planning.html', user=user, proyects=proyects)

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
    return redirect('/planning')

#  ---------------------------------- ADD JOBS -------------------------------------------------------

@app.route('/addjob/', methods=['POST'])
def addevent():

    if 'user_id' not in session:
        return redirect('/logout')
    
    project = Proyect.get_all_proyect_by_user_id({'id':session['user_id']})
    data ={}
    data['proyect_id'] = request.form['proyect_id']
    if len(project) > 0:
        for xl in project:
            if str(xl['id']) == data['proyect_id']:
                data['title'] = request.form['title']
                data['description'] = request.form['description']
                data['start'] = request.form['start-time-work']
                data['end'] = request.form['end-time-work']
            else: 
                print(str(xl['id']), data['proyect_id'])
        formato_original = "%Y-%m-%dT%H:%M"
        formato_sql = "%Y-%m-%d %H:%M:%S"
        data['start'] = datetime.strptime(data['start'], formato_original).strftime(formato_sql)
        data['end'] = datetime.strptime(data['end'], formato_original).strftime(formato_sql)
        print(data)
        Jobs.add_event(data)
        return redirect('/planning')
    else:
        print('No hay projectos')
        flash('No hay proyectos asociados')
    return redirect('/planning')

@app.route('/api/info_jobs', methods=['POST'])
def info_jobs():
    print(request.form['project_id'])
    xll = Jobs.get_all_jobs_by_proyect_id({'proyect_id':request.form['project_id']})
    jobs = Jobs.jobs_by_proyect_id({'proyect_id':request.form['project_id']})
    print(jobs)
    return jsonify(xll)