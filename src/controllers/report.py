# -*- coding: utf-8 -*-
import os
import time
from datetime import datetime
import smtplib
from io import BytesIO
import re   
from flask import render_template, redirect, session, request, jsonify, url_for, flash
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge, BadRequest
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from PIL import Image as PILImage, ImageOps

from src import app
from src.models.user import User
from src.models.proyects import Proyect
from src.models.reports import Report
from src.models.floors import Floor
from src.models.locals import Local

# ---------------------------------- Config correo ----------------------------------
app.config["SECRET_SALT"] = "mkonjibhu65544321"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'contacto@elisolutions.cl'
app.config['MAIL_PASSWORD'] = 'xjns snbu azpi wrml'

# ---------------------------------- UPLOADS unificado ----------------------------------
REL_UPLOADS = os.path.join("static", "uploads")              # siempre plural
UPLOAD_FOLDER = app.config.get("UPLOAD_FOLDER", REL_UPLOADS)
if not os.path.isabs(UPLOAD_FOLDER):
    UPLOAD_FOLDER = os.path.join(app.root_path, REL_UPLOADS)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Tamaño máximo de request (50 MB)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

# ---------------------------------- Extensiones permitidas ----------------------------------
ALLOWED_EXTENSIONS = {
    'png','jpg','jpeg','gif','bmp','webp','heic','heif','jfif','pjpeg','pjp','tif','tiff', 'HEIF'
}

# Bcrypt
bcrypt = Bcrypt(app)

# ---------------------------------- Views básicas ----------------------------------
@app.route('/report/')
def plan():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {'id': session['user_id']}
    user = User.get_by_id(data)
    mall = Report.get_all_shopping_by_user_id(data)
    return render_template('report.html', user=user, mall=mall)

# @app.route('/add_centro_comercial', methods=['POST'])
# def nuevo_centro():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     centro_raw = (request.form.get('centro_co') or '').strip()
#     if not centro_raw:
#         flash("Debes ingresar el nombre del centro comercial.", "error_add_centro")
#         return redirect('/report')
#     data = {'centro': centro_raw, 'user_id': session['user_id']}
#     Report.save_shopping(data)
#     flash("Centro Comercial agregado correctamente.", "success_add_centro")
#     return redirect('/report')

# @app.route('/add_piso', methods=['POST'])
# def nuevo_piso():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     piso_raw     = (request.form.get('piso') or '').strip()
#     trasc_raw    = (request.form.get('trasc') or '').strip()
#     shopping_raw = (request.form.get('shopping_id') or '').strip()
#     if not piso_raw or not trasc_raw or not shopping_raw:
#         flash("Debes completar todos los campos.", "error_add_piso")
#         return redirect('/report')
#     try:
#         piso_num = int(piso_raw)
#     except ValueError:
#         flash("El piso debe ser un número válido.", "error_add_piso")
#         return redirect('/report')
#     data = {
#         'floor': f"Piso {piso_num}",
#         'trasc': trasc_raw,
#         'shopping_id': shopping_raw,
#         'user_id': session['user_id']
#     }
#     Floor.add_floor(data)
#     flash(f"Piso {piso_num} agregado correctamente.", "success_add_piso")
#     return redirect('/report')

# @app.route('/add_local', methods=['POST'])
# def nuevo_local():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     marca      = (request.form.get('marca') or '').strip()
#     numero_raw = (request.form.get('numero') or '').strip()
#     floor_raw  = (request.form.get('floor_id') or '').strip()
#     if not marca or not numero_raw or not floor_raw:
#         flash("Debes completar todos los campos.", "error_add_local")
#         return redirect('/report')
#     try:
#         numero   = int(numero_raw)
#         floor_id = int(floor_raw)
#     except ValueError:
#         flash("Número y piso deben ser números válidos.", "error_add_local")
#         return redirect('/report')
#     data = {"marca": marca, "numero": numero, "floor_id": floor_id}
#     if not Local.validate_local(data):
#         flash("Datos inválidos. Revisa los campos ingresados.", "error_add_local")
#         return redirect('/report')
#     Local.add_local(data)
#     flash(f"Local {marca} N°{numero} agregado correctamente.", "success_add_local")
#     return redirect('/report')

# @app.route('/api/mall', methods=['POST'])
# def piso_por_mall():
#     floors = Floor.get_all_floor({"shopping_id": request.form.get("mall")})
#     return jsonify(floors)

# @app.route('/api/floors', methods=['POST'])
# def local():
#     locales = Local.get_all_local({"floor_id": request.form.get("floor")})
#     return jsonify(locales)

# ---------------------------------- Manejo tamaño request ----------------------------------
@app.errorhandler(RequestEntityTooLarge)
def handle_large_file(e):
    flash("El total de archivos supera el límite permitido.", "error_observacion")
    return redirect('/report')

# ---------------------------------- Imágenes para PDF ----------------------------------
IMG_CELL_W_PT = 260
IMG_CELL_H_PT = 200
TARGET_MAX_PX = 1800
TABLE_COL_W   = [280, 223]

def rl_image_from_upload(file_storage,
                         max_w_pt=IMG_CELL_W_PT,
                         max_h_pt=IMG_CELL_H_PT,
                         target_px=TARGET_MAX_PX) -> Image:
    img = ImageOps.exif_transpose(PILImage.open(file_storage.stream))
    img = img.convert("RGB")
    wpx, hpx = img.size
    if max(wpx, hpx) > target_px:
        scale = target_px / float(max(wpx, hpx))
        img = img.resize((int(wpx*scale), int(hpx*scale)), resample=PILImage.LANCZOS)
        wpx, hpx = img.size
    scale_pt = min(max_w_pt/float(wpx), max_h_pt/float(hpx), 1.0)
    wpt, hpt = int(wpx*scale_pt), int(hpx*scale_pt)

    bio = BytesIO()
    use_png = False
    try:
        if img.getcolors(maxcolors=256) is not None:
            use_png = True
    except Exception:
        use_png = False
    if use_png:
        img.save(bio, format="PNG", optimize=True)
    else:
        img.save(bio, format="JPEG", quality=95, optimize=True, subsampling=0)
    bio.seek(0)
    return Image(bio, width=wpt, height=hpt)

# ---------------------------------- Generar PDF + correo ----------------------------------

@app.route("/add_observacion", methods=["POST"])
def add_observacion():
    # Bloquea si no hay sesión
    if 'user_id' not in session:
        return redirect('/logout')

    print("=== add_observacion INICIO ===")

    def allowed_file(filename: str) -> bool:
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    try:
        # ---------- Lee el formulario con tolerancia ----------
        shopping_name = (request.form.get("shopping_id") or "").strip()  # ahora es TEXTO
        floor_name    = (request.form.get("floor_id") or "").strip()     # ahora es TEXTO
        local_name    = (request.form.get("local_id") or "").strip()     # ahora es TEXTO
        correos_raw   = (request.form.get("correo") or request.form.get("email_destino") or "").strip()

        print(f"[FORM] shopping='{shopping_name}' floor='{floor_name}' local='{local_name}' correos='{correos_raw}'")

        # Observaciones / Fotos (arrays)
        obs_texts = [(t or "").strip() for t in request.form.getlist("obs_text[]")]
        fotos     = request.files.getlist("obs_foto[]")
        print(f"[PAYLOAD] obs_texts={len(obs_texts)} fotos={len(fotos)} "
              f"filenames={[getattr(f,'filename','') for f in fotos]}")

    except BadRequest as e:
        # Si Flask falla parseando el multipart (típico origen de 400), lo detectamos y devolvemos un flash amable
        print("[REQUEST] BadRequest al parsear el formulario:", repr(e))
        flash("No se pudo procesar el formulario (multipart inválido). Reintenta tomando la foto nuevamente.", "error_observacion")
        return redirect('/report')

    # ---------- Validaciones mínimas ----------
    if not shopping_name or not floor_name or not local_name:
        flash("Faltan datos requeridos (Centro/Piso/Local).", "error_observacion")
        print("! Falta Centro/Piso/Local")
        return redirect('/report')

    # Correos: separa por comas/espacios y valida formato básico
    correos = [c.strip() for c in re.split(r'[,\s]+', correos_raw) if c.strip()]
    email_re = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    correos_validos = [c for c in correos if email_re.match(c)]
    if not correos_validos:
        flash("Debes ingresar al menos un correo válido.", "error_observacion")
        print("! Sin correos válidos")
        return redirect('/report')

    # Debe existir al menos una observación (texto o foto)
    tiene_texto = any((t or "").strip() for t in obs_texts)

    def archivo_subido(f):
        try:
            return bool(getattr(f, "filename", "").strip())
        except Exception:
            return False

    tiene_foto = any(archivo_subido(f) for f in fotos)

    if not (tiene_texto or tiene_foto):
        flash("Debes ingresar al menos una observación o adjuntar una foto.", "error_observacion")
        print("! No hay texto ni fotos")
        return redirect('/report')

    # ---------- Cabecera: tomamos nombre del usuario logeado ----------
    try:
        user_obj = User.get_by_id({"id": session["user_id"]})
        nombre   = getattr(user_obj, 'first_name', 'Usuario')
        apellido = getattr(user_obj, 'last_name', '')
    except Exception as e:
        print("[DB] No se pudo obtener usuario:", e)
        nombre, apellido = "Usuario", ""

    mall         = shopping_name
    piso         = floor_name
    local_full   = local_name  # ej: "Nike Store 2030" o "Nike 2020"

    # ---------- Generar nombre del PDF con local y centro ----------
    # Limpiar caracteres no válidos para nombres de archivo
    def clean_filename(text):
        return re.sub(r'[\\/*?:"<>|]', "", text).replace(" ", "_")
    
    mall_clean = clean_filename(mall)
    local_clean = clean_filename(local_full)
    fecha_str = datetime.now().strftime("%d%m%Y_%H%M")
    pdf_filename = f"Informe_{mall_clean}_{local_clean}_{fecha_str}.pdf"

    # ---------- Construcción del PDF en MEMORIA ----------
    pdf_buffer = BytesIO()
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(
        pdf_buffer,
        pagesize=A4,
        leftMargin=40, rightMargin=40, topMargin=74, bottomMargin=54
    )

    elements = []
    elements.append(Paragraph("<b>Informe de Observaciones</b>", styles['Title']))

    now = datetime.now()
    hora_formateada = now.strftime('%I:%M %p').lstrip('0').lower()
    fecha_hora = f"{now.strftime('%d/%m/%Y')} {hora_formateada}"

    texto_combinado = f"""
        <b>Coordinador:</b> {nombre} {apellido}<br/>
        <b>Fecha:</b> {fecha_hora}
    """
    info_data = [
        [Paragraph(texto_combinado, styles['Normal'])]
    ]
    info_table = Table(info_data, colWidths=['100%'])
    info_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'), # Todo alineado a la izquierda
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))

    elements.append(info_table)
    elements.append(Paragraph(f"<b>Centro Comercial:</b> Cenco {mall}", styles['Normal']))
    elements.append(Paragraph(f"<b>Nivel:</b> {piso}", styles['Normal']))
    elements.append(Paragraph(f"<b>Local:</b> {local_full}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Tabla (Fotografía | Descripción)
    data = [["Fotografía", "Descripción"]]
    filas = max(len(obs_texts), len(fotos))

    for i in range(filas):
        obs_text = (obs_texts[i] if i < len(obs_texts) else "").strip()
        if not obs_text:
            obs_text = "Sin descripción"

        img_cell = ""  # por defecto, celda vacía (no “Sin foto” ni error)

        file = fotos[i] if i < len(fotos) else None
        filename = (getattr(file, "filename", "") or "").strip()

        if file and filename:
            if allowed_file(filename):
                try:
                    # Usa tu helper que respeta orientación EXIF
                    img_cell = rl_image_from_upload(file, max_w_pt=IMG_CELL_W_PT, max_h_pt=IMG_CELL_H_PT)
                    print(f"[IMG] {i+1} OK → {filename}")
                except Exception as e:
                    # Si falla al dibujar, dejamos la celda VACÍA, sin mensaje de error
                    print(f"[IMG] {i+1} Observacion sin imagen adjunta")
                    img_cell = ""
            else:
                # Formato no permitido: dejamos la celda VACÍA, sin mensaje
                print(f"[IMG] {i+1} formato no permitido → {filename}")
                img_cell = ""

        data.append([img_cell, Paragraph(obs_text, styles["Normal"])])


    table = Table(data, colWidths=TABLE_COL_W)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0e1a4a")),  # azul oscuro header
        ('TEXTCOLOR',(0,0),(-1,0), colors.whitesmoke),

        # Centrar ambos encabezados/celdas
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),

        ('GRID', (0,0), (-1,-1), 0.5, colors.black),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('TOPPADDING', (0,1), (-1,-1), 2),
        ('BOTTOMPADDING', (0,1), (-1,-1), 2),
        ('LEFTPADDING', (0,1), (-1,-1), 3),
        ('RIGHTPADDING', (0,1), (-1,-1), 3),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 8))

    def draw_header(canvas, doc_):
        try:
            canvas.setPageCompression(1)
        except Exception:
            pass
        canvas.saveState()

        page_w, page_h = doc_.pagesize
        left   = 40
        top_y  = page_h - 36
        logo_w, logo_h = 140, 35

        try:
            logo_path = os.path.join(app.root_path, "static", "img", "cencomalls.png")
            if os.path.exists(logo_path):
                canvas.drawImage(
                    logo_path, left, top_y - logo_h,
                    width=logo_w, height=logo_h,
                    preserveAspectRatio=True, mask='auto'
                )
        except Exception as e:
            print("[HEADER] No se pudo dibujar el logo:", e)

        canvas.restoreState()

    def draw_footer(canvas, doc_):
        try:
            canvas.setPageCompression(1)
        except Exception:
            pass
        canvas.saveState()
        canvas.setFont("Helvetica", 12)
        footer_text = "Equipo de coordinación de locales · Cencomalls"
        canvas.drawCentredString(doc_.pagesize[0]/2.0, 50, footer_text)
        canvas.restoreState()

    # Build a memoria
    try:
        doc.build(
            elements,
            onFirstPage=lambda c, d: (draw_header(c, d), draw_footer(c, d)),
            onLaterPages=lambda c, d: (draw_header(c, d), draw_footer(c, d))
        )
    except Exception as e:
        print("[PDF] Error ReportLab:", e)
        flash("Error al generar el PDF.", "error_observacion")
        return redirect('/report')

    pdf_buffer.seek(0)  # ¡importante! posiciona al inicio para leerlo

    # ---------- Envío de correo (a varios destinatarios) ----------
    try:
        msg = MIMEMultipart()
        msg['From']    = app.config['MAIL_USERNAME']
        msg['To']      = ", ".join(correos_validos)
        msg['Subject'] = f"Informe de Observaciones - {local_full} - {mall}"

        body = f"""Hola,

Se adjunta el informe de observaciones del local {local_full} en Cenco {mall}.

Saludos,
Equipo de coordinación de locales · Cencomalls"""
        msg.attach(MIMEText(body, 'plain'))

        part = MIMEBase("application", "pdf")
        part.set_payload(pdf_buffer.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={pdf_filename}")
        msg.attach(part)

        server = smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT'])
        if app.config.get('MAIL_USE_TLS', True):
            server.starttls()
        server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        server.sendmail(app.config['MAIL_USERNAME'], correos_validos, msg.as_string())
        server.quit()

        print(f"[SMTP] OK → {correos_validos}")
        
        # Respuesta JSON de éxito (mensaje según cantidad de correos)
        if len(correos_validos) == 1:
            mensaje_exito = f"Informe generado y enviado al único correo ingresado: {correos_validos[0]}"
        else:
            mensaje_exito = f"Informe generado y enviado a todos los correos"

        return jsonify({'status': 'success', 'message': mensaje_exito})


    except Exception as e:
        print("[SMTP] ERROR:", e)
        mensaje_error = "El informe se generó, pero falló el envío por correo."
        return jsonify({'status': 'error', 'message': mensaje_error})



