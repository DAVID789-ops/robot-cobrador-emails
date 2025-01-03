import smtplib
import datetime
import requests
import os
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from config.settings import EMAIL_CONFIG

print("Envío de correos en frances ----------------------")
def descargar_pdf(pdf_url, nombre_pdf):
    """
    Función que descarga un archivo PDF desde una URL.
    Si la URL no tiene un esquema, agrega un dominio por defecto.
    """
    # Verificar si la URL tiene esquema (https:// o http://)
    if not pdf_url.startswith("http://") and not pdf_url.startswith("https://"):
        pdf_url = "https://legion.webimpresionante.com/storage/" + pdf_url  # Agregar el dominio si no está presente

    try:
        # Configurar encabezados de la solicitud para evitar el error 406
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept": "application/pdf"
        }
        
        # Realizar la solicitud para obtener el PDF
        response = requests.get(pdf_url, headers=headers)
        
        if response.status_code == 200:
            # Guardar el contenido del archivo PDF
            with open(nombre_pdf, "wb") as f:
                f.write(response.content)
            print(f"PDF descargado correctamente: {nombre_pdf}")
            return nombre_pdf
        else:
            print(f"Error al descargar el PDF. Código de estado: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error al descargar el archivo: {e}")
        return None

def enviar_correos(deudas):
    """
    Función que envía correos de recordatorio de pago pendiente a los contactos 
    que cumplan con los criterios establecidos.
    """
    # Obtener el día de la semana
    dia_semana = datetime.datetime.now().weekday()



#     //////////////////     aqui empieza el IDIOMA frances -----------------------
#
#
#
# intensidad 1 frances 3 dias a la semana
    # Verificar si es lunes, miércoles o viernes (0, 2, 4)
    if dia_semana in [0, 2, 4]:
        print("Hoy es lunes, miércoles o viernes. Se procederá con el tercer intento.")
        
        try:
            # Conexión al servidor SMTP
            servidor = smtplib.SMTP_SSL(EMAIL_CONFIG["SMTP_SERVER"], EMAIL_CONFIG["SMTP_PORT"])
            servidor.login(EMAIL_CONFIG["USER"], EMAIL_CONFIG["PASSWORD"])
            

            for deuda in deudas:
                nombre_colegio, cantidad_deuda, producto_entregado, fecha_entrega, email_contacto, signo, intensidad, idioma, tiempo, pdf_documento, cobrar = deuda

                # Verificar las condiciones para enviar el correo (intensidad 2, frances, tiempo 3)
                if intensidad == 1 and idioma.lower() == "frances" and tiempo == 3 and cobrar == True:
                    
                    # Crear el mensaje del correo
                    mensaje = MIMEMultipart()
                    mensaje["From"] = EMAIL_CONFIG["USER"]
                    mensaje["To"] = email_contacto
                    mensaje["Subject"] = f"Rappel de Paiement en Souffrance - {nombre_colegio}"

                    # Cargar el contenido HTML del correo
                    with open("emails/templates/frances/1/carta.html", "r", encoding="utf-8") as f:
                        html = f.read().format(
                            nombre_colegio=nombre_colegio,
                            cantidad_deuda=cantidad_deuda,
                            producto_entregado=producto_entregado,
                            fecha_entrega=fecha_entrega,
                            signo=signo
                        )

                    mensaje.attach(MIMEText(html, "html", _charset="utf-8"))

                    # Adjuntar el logo al correo
                    with open("emails/templates/frances/1/logo.png", "rb") as img:
                        logo = MIMEImage(img.read())
                        logo.add_header("Content-ID", "<logo>")
                        mensaje.attach(logo)

                    # Adjuntar la imagen del pie de página
                    with open("emails/templates/frances/1/footer_image.png", "rb") as img:
                        footer_image = MIMEImage(img.read())
                        footer_image.add_header("Content-ID", "<footer_image>")
                        mensaje.attach(footer_image)

                    # Si se proporciona un documento PDF, descargarlo y adjuntarlo
                    if pdf_documento:
                        pdf_file_name = "documento_deuda.pdf"
                        archivo_pdf = descargar_pdf(pdf_documento, pdf_file_name)

                        if archivo_pdf:
                            # Adjuntar el archivo PDF al correo
                            with open(archivo_pdf, "rb") as archivo:
                                adjunto_pdf = MIMEBase("application", "octet-stream")
                                adjunto_pdf.set_payload(archivo.read())
                                encoders.encode_base64(adjunto_pdf)
                                adjunto_pdf.add_header("Content-Disposition", f"attachment; filename={pdf_file_name}")
                                mensaje.attach(adjunto_pdf)

                            # Eliminar el archivo PDF después de enviarlo
                            os.remove(archivo_pdf)

                    # Enviar el correo
                    servidor.sendmail(EMAIL_CONFIG["USER"], email_contacto, mensaje.as_string())
                    print(f"Correo enviado a {nombre_colegio} ({email_contacto})")

            # Cerrar la conexión con el servidor SMTP
            servidor.quit()

        except Exception as e:
            print(f"Error al enviar correos (tercer intento): {e}")





# intensidad 1 frances 2 dias a la semana EXPAÑOL

    if dia_semana in [0, 3]:
        print("Hoy es lunes o JUEVES. Se procederá con el 2DO BLOQUE.")
        
        try:
            # Conexión al servidor SMTP
            servidor = smtplib.SMTP_SSL(EMAIL_CONFIG["SMTP_SERVER"], EMAIL_CONFIG["SMTP_PORT"])
            servidor.login(EMAIL_CONFIG["USER"], EMAIL_CONFIG["PASSWORD"])
            

            for deuda in deudas:
                nombre_colegio, cantidad_deuda, producto_entregado, fecha_entrega, email_contacto, signo, intensidad, idioma, tiempo, pdf_documento, cobrar = deuda

                # Verificar las condiciones para enviar el correo (intensidad 1, frances, tiempo 2)
                if intensidad == 1 and idioma.lower() == "frances" and tiempo == 2 and cobrar == True:
                    
                    # Crear el mensaje del correo
                    mensaje = MIMEMultipart()
                    mensaje["From"] = EMAIL_CONFIG["USER"]
                    mensaje["To"] = email_contacto
                    mensaje["Subject"] = f"Rappel de Paiement en Souffrance - {nombre_colegio}"

                    # Cargar el contenido HTML del correo
                    with open("emails/templates/frances/1/carta.html", "r", encoding="utf-8") as f:
                        html = f.read().format(
                            nombre_colegio=nombre_colegio,
                            cantidad_deuda=cantidad_deuda,
                            producto_entregado=producto_entregado,
                            fecha_entrega=fecha_entrega,
                            signo=signo
                        )

                    mensaje.attach(MIMEText(html, "html", _charset="utf-8"))

                    # Adjuntar el logo al correo
                    with open("emails/templates/frances/1/logo.png", "rb") as img:
                        logo = MIMEImage(img.read())
                        logo.add_header("Content-ID", "<logo>")
                        mensaje.attach(logo)

                    # Adjuntar la imagen del pie de página
                    with open("emails/templates/frances/1/footer_image.png", "rb") as img:
                        footer_image = MIMEImage(img.read())
                        footer_image.add_header("Content-ID", "<footer_image>")
                        mensaje.attach(footer_image)

                    # Si se proporciona un documento PDF, descargarlo y adjuntarlo
                    if pdf_documento:
                        pdf_file_name = "documento_deuda.pdf"
                        archivo_pdf = descargar_pdf(pdf_documento, pdf_file_name)

                        if archivo_pdf:
                            # Adjuntar el archivo PDF al correo
                            with open(archivo_pdf, "rb") as archivo:
                                adjunto_pdf = MIMEBase("application", "octet-stream")
                                adjunto_pdf.set_payload(archivo.read())
                                encoders.encode_base64(adjunto_pdf)
                                adjunto_pdf.add_header("Content-Disposition", f"attachment; filename={pdf_file_name}")
                                mensaje.attach(adjunto_pdf)

                            # Eliminar el archivo PDF después de enviarlo
                            os.remove(archivo_pdf)

                    # Enviar el correo
                    servidor.sendmail(EMAIL_CONFIG["USER"], email_contacto, mensaje.as_string())
                    print(f"Correo enviado a {nombre_colegio} ({email_contacto})")

            # Cerrar la conexión con el servidor SMTP
            servidor.quit()

        except Exception as e:
            print(f"Error al enviar correos (tercer intento): {e}")

# intensidad 1 frances 1 dia a la semana EXPAÑOL TIEMPO 1

    if dia_semana == 0:
        print("Hoy es lunes. Se procederá con el tercer intento.")
        
        try:
            # Conexión al servidor SMTP
            servidor = smtplib.SMTP_SSL(EMAIL_CONFIG["SMTP_SERVER"], EMAIL_CONFIG["SMTP_PORT"])
            servidor.login(EMAIL_CONFIG["USER"], EMAIL_CONFIG["PASSWORD"])
            

            for deuda in deudas:
                nombre_colegio, cantidad_deuda, producto_entregado, fecha_entrega, email_contacto, signo, intensidad, idioma, tiempo, pdf_documento, cobrar = deuda

                # Verificar las condiciones para enviar el correo (intensidad 1, frances, tiempo 2)
                if intensidad == 1 and idioma.lower() == "frances" and tiempo == 1 and cobrar == True:
                    
                    # Crear el mensaje del correo
                    mensaje = MIMEMultipart()
                    mensaje["From"] = EMAIL_CONFIG["USER"]
                    mensaje["To"] = email_contacto
                    mensaje["Subject"] = f"Rappel de Paiement en Souffrance - {nombre_colegio}"

                    # Cargar el contenido HTML del correo
                    with open("emails/templates/frances/1/carta.html", "r", encoding="utf-8") as f:
                        html = f.read().format(
                            nombre_colegio=nombre_colegio,
                            cantidad_deuda=cantidad_deuda,
                            producto_entregado=producto_entregado,
                            fecha_entrega=fecha_entrega,
                            signo=signo
                        )

                    mensaje.attach(MIMEText(html, "html", _charset="utf-8"))

                    # Adjuntar el logo al correo
                    with open("emails/templates/frances/1/logo.png", "rb") as img:
                        logo = MIMEImage(img.read())
                        logo.add_header("Content-ID", "<logo>")
                        mensaje.attach(logo)

                    # Adjuntar la imagen del pie de página
                    with open("emails/templates/frances/1/footer_image.png", "rb") as img:
                        footer_image = MIMEImage(img.read())
                        footer_image.add_header("Content-ID", "<footer_image>")
                        mensaje.attach(footer_image)

                    # Si se proporciona un documento PDF, descargarlo y adjuntarlo
                    if pdf_documento:
                        pdf_file_name = "documento_deuda.pdf"
                        archivo_pdf = descargar_pdf(pdf_documento, pdf_file_name)

                        if archivo_pdf:
                            # Adjuntar el archivo PDF al correo
                            with open(archivo_pdf, "rb") as archivo:
                                adjunto_pdf = MIMEBase("application", "octet-stream")
                                adjunto_pdf.set_payload(archivo.read())
                                encoders.encode_base64(adjunto_pdf)
                                adjunto_pdf.add_header("Content-Disposition", f"attachment; filename={pdf_file_name}")
                                mensaje.attach(adjunto_pdf)

                            # Eliminar el archivo PDF después de enviarlo
                            os.remove(archivo_pdf)

                    # Enviar el correo
                    servidor.sendmail(EMAIL_CONFIG["USER"], email_contacto, mensaje.as_string())
                    print(f"Correo enviado a {nombre_colegio} ({email_contacto})")

            # Cerrar la conexión con el servidor SMTP
            servidor.quit()

        except Exception as e:
            print(f"Error al enviar correos (tercer intento): {e}")

    

















#
#        ///////////////////////   aqui empiza intensidad 2
#
# intensidad 2 frances 3 dias a la semana
    # Verificar si es lunes, miércoles o viernes (0, 2, 4)
    if dia_semana in [0, 2, 4]:
        print("Hoy es lunes, miércoles o viernes. Se procederá con el tercer intento.")
        
        try:
            # Conexión al servidor SMTP
            servidor = smtplib.SMTP_SSL(EMAIL_CONFIG["SMTP_SERVER"], EMAIL_CONFIG["SMTP_PORT"])
            servidor.login(EMAIL_CONFIG["USER"], EMAIL_CONFIG["PASSWORD"])
            

            for deuda in deudas:
                nombre_colegio, cantidad_deuda, producto_entregado, fecha_entrega, email_contacto, signo, intensidad, idioma, tiempo, pdf_documento, cobrar = deuda

                # Verificar las condiciones para enviar el correo (intensidad 2, frances, tiempo 3)
                if intensidad == 2 and idioma.lower() == "frances" and tiempo == 3 and cobrar == True:
                    
                    # Crear el mensaje del correo
                    mensaje = MIMEMultipart()
                    mensaje["From"] = EMAIL_CONFIG["USER"]
                    mensaje["To"] = email_contacto
                    mensaje["Subject"] = f"Rappel de Paiement en Souffrance - {nombre_colegio}"

                    # Cargar el contenido HTML del correo
                    with open("emails/templates/frances/2/carta.html", "r", encoding="utf-8") as f:
                        html = f.read().format(
                            nombre_colegio=nombre_colegio,
                            cantidad_deuda=cantidad_deuda,
                            producto_entregado=producto_entregado,
                            fecha_entrega=fecha_entrega,
                            signo=signo
                        )

                    mensaje.attach(MIMEText(html, "html", _charset="utf-8"))

                    # Adjuntar el logo al correo
                    with open("emails/templates/frances/2/logo.png", "rb") as img:
                        logo = MIMEImage(img.read())
                        logo.add_header("Content-ID", "<logo>")
                        mensaje.attach(logo)

                    # Adjuntar la imagen del pie de página
                    with open("emails/templates/frances/2/footer_image.png", "rb") as img:
                        footer_image = MIMEImage(img.read())
                        footer_image.add_header("Content-ID", "<footer_image>")
                        mensaje.attach(footer_image)

                    # Si se proporciona un documento PDF, descargarlo y adjuntarlo
                    if pdf_documento:
                        pdf_file_name = "documento_deuda.pdf"
                        archivo_pdf = descargar_pdf(pdf_documento, pdf_file_name)

                        if archivo_pdf:
                            # Adjuntar el archivo PDF al correo
                            with open(archivo_pdf, "rb") as archivo:
                                adjunto_pdf = MIMEBase("application", "octet-stream")
                                adjunto_pdf.set_payload(archivo.read())
                                encoders.encode_base64(adjunto_pdf)
                                adjunto_pdf.add_header("Content-Disposition", f"attachment; filename={pdf_file_name}")
                                mensaje.attach(adjunto_pdf)

                            # Eliminar el archivo PDF después de enviarlo
                            os.remove(archivo_pdf)

                    # Enviar el correo
                    servidor.sendmail(EMAIL_CONFIG["USER"], email_contacto, mensaje.as_string())
                    print(f"Correo enviado a {nombre_colegio} ({email_contacto})")

            # Cerrar la conexión con el servidor SMTP
            servidor.quit()

        except Exception as e:
            print(f"Error al enviar correos (tercer intento): {e}")





# intensidad 2 frances 2 dias a la semana EXPAÑOL

    if dia_semana in [0, 3]:
        print("Hoy es lunes o JUEVES. Se procederá con el 2DO BLOQUE.")
        
        try:
            # Conexión al servidor SMTP
            servidor = smtplib.SMTP_SSL(EMAIL_CONFIG["SMTP_SERVER"], EMAIL_CONFIG["SMTP_PORT"])
            servidor.login(EMAIL_CONFIG["USER"], EMAIL_CONFIG["PASSWORD"])
            

            for deuda in deudas:
                nombre_colegio, cantidad_deuda, producto_entregado, fecha_entrega, email_contacto, signo, intensidad, idioma, tiempo, pdf_documento, cobrar = deuda

                # Verificar las condiciones para enviar el correo (intensidad 2, frances, tiempo 2)
                if intensidad == 2 and idioma.lower() == "frances" and tiempo == 2 and cobrar == True:
                    
                    # Crear el mensaje del correo
                    mensaje = MIMEMultipart()
                    mensaje["From"] = EMAIL_CONFIG["USER"]
                    mensaje["To"] = email_contacto
                    mensaje["Subject"] = f"Rappel de Paiement en Souffrance - {nombre_colegio}"

                    # Cargar el contenido HTML del correo
                    with open("emails/templates/frances/2/carta.html", "r", encoding="utf-8") as f:
                        html = f.read().format(
                            nombre_colegio=nombre_colegio,
                            cantidad_deuda=cantidad_deuda,
                            producto_entregado=producto_entregado,
                            fecha_entrega=fecha_entrega,
                            signo=signo
                        )

                    mensaje.attach(MIMEText(html, "html", _charset="utf-8"))

                    # Adjuntar el logo al correo
                    with open("emails/templates/frances/2/logo.png", "rb") as img:
                        logo = MIMEImage(img.read())
                        logo.add_header("Content-ID", "<logo>")
                        mensaje.attach(logo)

                    # Adjuntar la imagen del pie de página
                    with open("emails/templates/frances/2/footer_image.png", "rb") as img:
                        footer_image = MIMEImage(img.read())
                        footer_image.add_header("Content-ID", "<footer_image>")
                        mensaje.attach(footer_image)

                    # Si se proporciona un documento PDF, descargarlo y adjuntarlo
                    if pdf_documento:
                        pdf_file_name = "documento_deuda.pdf"
                        archivo_pdf = descargar_pdf(pdf_documento, pdf_file_name)

                        if archivo_pdf:
                            # Adjuntar el archivo PDF al correo
                            with open(archivo_pdf, "rb") as archivo:
                                adjunto_pdf = MIMEBase("application", "octet-stream")
                                adjunto_pdf.set_payload(archivo.read())
                                encoders.encode_base64(adjunto_pdf)
                                adjunto_pdf.add_header("Content-Disposition", f"attachment; filename={pdf_file_name}")
                                mensaje.attach(adjunto_pdf)

                            # Eliminar el archivo PDF después de enviarlo
                            os.remove(archivo_pdf)

                    # Enviar el correo
                    servidor.sendmail(EMAIL_CONFIG["USER"], email_contacto, mensaje.as_string())
                    print(f"Correo enviado a {nombre_colegio} ({email_contacto})")

            # Cerrar la conexión con el servidor SMTP
            servidor.quit()

        except Exception as e:
            print(f"Error al enviar correos (tercer intento): {e}")

# intensidad 2 frances 1 dia a la semana EXPAÑOL TIEMPO 1

    if dia_semana == 0:
        print("Hoy es lunes. Se procederá con el tercer intento.")
        
        try:
            # Conexión al servidor SMTP
            servidor = smtplib.SMTP_SSL(EMAIL_CONFIG["SMTP_SERVER"], EMAIL_CONFIG["SMTP_PORT"])
            servidor.login(EMAIL_CONFIG["USER"], EMAIL_CONFIG["PASSWORD"])
            

            for deuda in deudas:
                nombre_colegio, cantidad_deuda, producto_entregado, fecha_entrega, email_contacto, signo, intensidad, idioma, tiempo, pdf_documento, cobrar = deuda

                # Verificar las condiciones para enviar el correo (intensidad 2, frances, tiempo 2)
                if intensidad == 2 and idioma.lower() == "frances" and tiempo == 1 and cobrar == True:
                    
                    # Crear el mensaje del correo
                    mensaje = MIMEMultipart()
                    mensaje["From"] = EMAIL_CONFIG["USER"]
                    mensaje["To"] = email_contacto
                    mensaje["Subject"] = f"Rappel de Paiement en Souffrance - {nombre_colegio}"

                    # Cargar el contenido HTML del correo
                    with open("emails/templates/frances/2/carta.html", "r", encoding="utf-8") as f:
                        html = f.read().format(
                            nombre_colegio=nombre_colegio,
                            cantidad_deuda=cantidad_deuda,
                            producto_entregado=producto_entregado,
                            fecha_entrega=fecha_entrega,
                            signo=signo
                        )

                    mensaje.attach(MIMEText(html, "html", _charset="utf-8"))

                    # Adjuntar el logo al correo
                    with open("emails/templates/frances/2/logo.png", "rb") as img:
                        logo = MIMEImage(img.read())
                        logo.add_header("Content-ID", "<logo>")
                        mensaje.attach(logo)

                    # Adjuntar la imagen del pie de página
                    with open("emails/templates/frances/2/footer_image.png", "rb") as img:
                        footer_image = MIMEImage(img.read())
                        footer_image.add_header("Content-ID", "<footer_image>")
                        mensaje.attach(footer_image)

                    # Si se proporciona un documento PDF, descargarlo y adjuntarlo
                    if pdf_documento:
                        pdf_file_name = "documento_deuda.pdf"
                        archivo_pdf = descargar_pdf(pdf_documento, pdf_file_name)

                        if archivo_pdf:
                            # Adjuntar el archivo PDF al correo
                            with open(archivo_pdf, "rb") as archivo:
                                adjunto_pdf = MIMEBase("application", "octet-stream")
                                adjunto_pdf.set_payload(archivo.read())
                                encoders.encode_base64(adjunto_pdf)
                                adjunto_pdf.add_header("Content-Disposition", f"attachment; filename={pdf_file_name}")
                                mensaje.attach(adjunto_pdf)

                            # Eliminar el archivo PDF después de enviarlo
                            os.remove(archivo_pdf)

                    # Enviar el correo
                    servidor.sendmail(EMAIL_CONFIG["USER"], email_contacto, mensaje.as_string())
                    print(f"Correo enviado a {nombre_colegio} ({email_contacto})")

            # Cerrar la conexión con el servidor SMTP
            servidor.quit()

        except Exception as e:
            print(f"Error al enviar correos (tercer intento): {e}")

