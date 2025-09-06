from flask import render_template,redirect,session,request, flash, url_for
from src import app
from src.models.user import User
from flask_bcrypt import Bcrypt
from itsdangerous import URLSafeTimedSerializer
import smtplib, time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
bcrypt = Bcrypt(app)

app.config["SECRET_KEY"] = "wedefergewvgetrgw492890348t2vnwc"
app.config["SECRET_SALT"] = "mkonjibhu65544321"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'contacto@elisolutions.cl'
app.config['MAIL_PASSWORD'] = 'xjns snbu azpi wrml'


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user:
        flash("Email Invalido","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Password invalida","login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/new_register',methods=['POST'])
def new_register():

    if not User.validate_new_register(request.form):
        return redirect('/register')
    
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "company": request.form['company'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password']),
    }
    User.save(data)
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    user = User.get_by_id(data)
    return render_template('dashboard.html', user=user)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# --------------------- RESET PASSWORD ------------------

# generar token para enviar por mail ------ 

def generate_reset_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECRET_SALT'])

def verify_reset_token(token, expiration=600):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=app.config['SECRET_SALT'],
            max_age=expiration
        )
    except Exception as e:
        print(f"Error al verificar el token: {e}")
        return None
    return email


# ---- VIEW FOR RECEIVE EMAIL ------

@app.route('/reset_password')
def reset():
    return render_template("reset_password.html")

# ---- LINK FOR RESET PASSWORD SEND FOR EMAIL-----

@app.route('/link_reset/<token>')
def newPassword(token):
    return render_template("reset_link.html", token=token)

# ------ CHANGE NEW PASSWORD -------------------- 

@app.route("/new_password/<token>" , methods=["POST"])
def successPass(token):
    email = verify_reset_token(token)
    if not email:
        flash("El token es inválido o ha expirado.", "change")
        print("error")
    if not User.validate_new_password(request.form):
        return render_template("reset_link.html", token=token) 
    data = {
        "password": bcrypt.generate_password_hash(request.form['passwordx']),
        "email": email,
    }
    print(data)
    User.update_password(data)
    flash("Tu contraseña ha sido cambiada con éxito.", "good")
    return redirect("/")

# ----------- VALIDATE EMAIL AND SEND LINK --------------

@app.route('/email_reset', methods=["POST"])
def recovery_password():
    user = User.get_by_email({"email": request.form["email"]})
    if not user:
        flash("Correo electrónico no encontrado.", "reset")
        return redirect("/reset_password")
    token = generate_reset_token(request.form["email"])
    reset_url = url_for('newPassword', token=token, _external=True)
    send_reset_email(request.form["email"], reset_url)
    flash("Te hemos enviado al correo un enlace para restablecer tu contraseña.", "success")
    return redirect("/reset_password")


def send_reset_email(to_email, reset_url):
    subject = "Restablece tu contraseña"
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = app.config['MAIL_USERNAME']
    msg['To'] = to_email

# --------TEXTO---------------------

    text = f"""\
    Hola,

    Has solicitado restablecer tu contraseña. Haz clic en el siguiente enlace para restablecerla:

    {reset_url}

    Si no solicitaste este cambio, por favor ignora este correo.

    Saludos,
    El equipo de soporte
    """

#   ------------HTML------------
    html = f"""\
    <html>
    <body>
        <h2>Hola,</h2>
        <p>Has solicitado restablecer tu contraseña. Haz clic en el enlace a continuación para restablecerla:</p>
        <p><a href="{reset_url}" style="background-color: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Restablecer Contraseña</a></p>
        <p>Si no solicitaste este cambio, simplemente ignora este correo.</p>
        <br>
        <p>Saludos,<br>El equipo de soporte Elisolutions</p>
    </body>
    </html>
    """

    # Adjuntar ambas partes
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    with smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT']) as server:
        server.starttls()
        server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        server.sendmail(app.config['MAIL_USERNAME'], to_email, msg.as_string())





