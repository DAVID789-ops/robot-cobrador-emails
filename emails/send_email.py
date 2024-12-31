import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from config.settings import EMAIL_CONFIG

def enviar_correos(deudas):
    # Obtener el día de la semana
    dia_semana = datetime.datetime.now().weekday()

    # Primer bloque: Lunes
    if dia_semana == 0:  # 0 es lunes
        print("Hoy es lunes, se procederá con el primer intento.")
        try:
            servidor = smtplib.SMTP_SSL(EMAIL_CONFIG["SMTP_SERVER"], EMAIL_CONFIG["SMTP_PORT"])
            servidor.login(EMAIL_CONFIG["USER"], EMAIL_CONFIG["PASSWORD"])

            for deuda in deudas:
                nombre_colegio, cantidad_deuda, producto_entregado, fecha_entrega, email_contacto, signo, intensidad, idioma, tiempo = deuda

                # Verificar las condiciones para lunes
                if intensidad == 2 and idioma.lower() == "español" and tiempo == 1:
                    # Crear el correo
                    mensaje = MIMEMultipart()
                    mensaje["From"] = EMAIL_CONFIG["USER"]
                    mensaje["To"] = email_contacto
                    mensaje["Subject"] = f"Recordatorio de Pago Pendiente - {nombre_colegio}"

                    # Generar contenido del correo
                    with open("emails/templates/español/2/reminder.html", "r", encoding="utf-8") as f:
                        html = f.read().format(
                            nombre_colegio=nombre_colegio,
                            cantidad_deuda=cantidad_deuda,
                            producto_entregado=producto_entregado,
                            fecha_entrega=fecha_entrega,
                            signo=signo
                        )

                    mensaje.attach(MIMEText(html, "html", _charset="utf-8"))

                    # Adjuntar el logo
                    with open("emails/templates/español/2/logo.png", "rb") as img:
                        logo = MIMEImage(img.read())
                        logo.add_header("Content-ID", "<logo>")
                        mensaje.attach(logo)

                    # Adjuntar imagen del pie de página
                    with open("emails/templates/español/2/footer_image.png", "rb") as img:
                        footer_image = MIMEImage(img.read())
                        footer_image.add_header("Content-ID", "<footer_image>")
                        mensaje.attach(footer_image)

                    servidor.sendmail(EMAIL_CONFIG["USER"], email_contacto, mensaje.as_string())
                    print(f"Correo enviado a {nombre_colegio} ({email_contacto})")

            servidor.quit()

        except Exception as e:
            print(f"Error al enviar correos (primer intento): {e}")

    # Segundo bloque: lunes o Jueves
    if dia_semana in [0, 3]:  # 0 es lunes, 3 es jueves
        print("Hoy es martes o jueves, se procederá con el segundo intento.")
        try:
            servidor = smtplib.SMTP_SSL(EMAIL_CONFIG["SMTP_SERVER"], EMAIL_CONFIG["SMTP_PORT"])
            servidor.login(EMAIL_CONFIG["USER"], EMAIL_CONFIG["PASSWORD"])

            for deuda in deudas:
                nombre_colegio, cantidad_deuda, producto_entregado, fecha_entrega, email_contacto, signo, intensidad, idioma, tiempo = deuda

                # Verificar las condiciones para martes o jueves
                if intensidad == 2 and idioma.lower() == "español" and tiempo == 2:
                    # Crear el correo
                    mensaje = MIMEMultipart()
                    mensaje["From"] = EMAIL_CONFIG["USER"]
                    mensaje["To"] = email_contacto
                    mensaje["Subject"] = f"Recordatorio de Pago Pendiente - {nombre_colegio}"

                    # Generar contenido del correo
                    with open("emails/templates/español/2/reminder.html", "r", encoding="utf-8") as f:
                        html = f.read().format(
                            nombre_colegio=nombre_colegio,
                            cantidad_deuda=cantidad_deuda,
                            producto_entregado=producto_entregado,
                            fecha_entrega=fecha_entrega,
                            signo=signo
                        )

                    mensaje.attach(MIMEText(html, "html", _charset="utf-8"))

                    # Adjuntar el logo
                    with open("emails/templates/español/2/logo.png", "rb") as img:
                        logo = MIMEImage(img.read())
                        logo.add_header("Content-ID", "<logo>")
                        mensaje.attach(logo)

                    # Adjuntar imagen del pie de página
                    with open("emails/templates/español/2/footer_image.png", "rb") as img:
                        footer_image = MIMEImage(img.read())
                        footer_image.add_header("Content-ID", "<footer_image>")
                        mensaje.attach(footer_image)

                    servidor.sendmail(EMAIL_CONFIG["USER"], email_contacto, mensaje.as_string())
                    print(f"Correo enviado a {nombre_colegio} ({email_contacto})")

            servidor.quit()

        except Exception as e:
            print(f"Error al enviar correos (segundo intento): {e}")

    # Tercer bloque: Para otros días
    if dia_semana in [0, 2, 4]:  # Si  es lunes, miercoles 0 viernes
        print("Hoy es lunes, miercoles o viernes. Se procederá con el tercer intento.")
        try:
            servidor = smtplib.SMTP_SSL(EMAIL_CONFIG["SMTP_SERVER"], EMAIL_CONFIG["SMTP_PORT"])
            servidor.login(EMAIL_CONFIG["USER"], EMAIL_CONFIG["PASSWORD"])

            for deuda in deudas:
                nombre_colegio, cantidad_deuda, producto_entregado, fecha_entrega, email_contacto, signo, intensidad, idioma, tiempo = deuda

                # Verificar las condiciones para otros días
                if intensidad == 2 and idioma.lower() == "español" and tiempo == 3:
                    # Crear el correo
                    mensaje = MIMEMultipart()
                    mensaje["From"] = EMAIL_CONFIG["USER"]
                    mensaje["To"] = email_contacto
                    mensaje["Subject"] = f"Recordatorio de Pago Pendiente - {nombre_colegio}"

                    # Generar contenido del correo
                    with open("emails/templates/español/2/reminder.html", "r", encoding="utf-8") as f:
                        html = f.read().format(
                            nombre_colegio=nombre_colegio,
                            cantidad_deuda=cantidad_deuda,
                            producto_entregado=producto_entregado,
                            fecha_entrega=fecha_entrega,
                            signo=signo
                        )

                    mensaje.attach(MIMEText(html, "html", _charset="utf-8"))

                    # Adjuntar el logo
                    with open("emails/templates/español/2/logo.png", "rb") as img:
                        logo = MIMEImage(img.read())
                        logo.add_header("Content-ID", "<logo>")
                        mensaje.attach(logo)

                    # Adjuntar imagen del pie de página
                    with open("emails/templates/español/2/footer_image.png", "rb") as img:
                        footer_image = MIMEImage(img.read())
                        footer_image.add_header("Content-ID", "<footer_image>")
                        mensaje.attach(footer_image)

                    servidor.sendmail(EMAIL_CONFIG["USER"], email_contacto, mensaje.as_string())
                    print(f"Correo enviado a {nombre_colegio} ({email_contacto})")

            servidor.quit()

        except Exception as e:
            print(f"Error al enviar correos (tercer intento): {e}")



            
