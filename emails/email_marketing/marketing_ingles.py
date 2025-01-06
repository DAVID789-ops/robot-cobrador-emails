import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from config.settings import EMAIL_CONFIG_MARKETING

def enviar_correos(marketing):
    """
    Envía correos a contactos según criterios específicos de marketing.
    """
    # Obtener el día actual
    dia_semana = datetime.datetime.now().weekday()

    # Verificar si el día es válido para el envío (Lunes, Miércoles, Viernes)
    if dia_semana not in [0, 2, 4]:
        print("Hoy no es un día programado para enviar correos.")
        return

    print("Hoy es lunes, miércoles o viernes. Se procederá con el envío de correos.")

    # Cargar la plantilla HTML y recursos una vez
    try:
        with open("emails/templates/marketing/ingles/carta.html", "r", encoding="utf-8") as f:
            plantilla_html = f.read()

        with open("emails/templates/marketing/ingles/logo.png", "rb") as img:
            logo = MIMEImage(img.read())
            logo.add_header("Content-ID", "<logo>")
      
        # Conexión al servidor SMTP
        with smtplib.SMTP_SSL(EMAIL_CONFIG_MARKETING["SMTP_SERVER"], EMAIL_CONFIG_MARKETING["SMTP_PORT"]) as servidor:
            servidor.login(EMAIL_CONFIG_MARKETING["USER"], EMAIL_CONFIG_MARKETING["PASSWORD"])

            for item in marketing:
                nombre_colegio, email_contacto, idioma, email_marketing = item

                # Comprobar si el idioma es español y el marketing está habilitado
                if idioma.lower() == "ingles" and email_marketing:
                    # Personalizar el mensaje HTML
                    html = plantilla_html.format(nombre_colegio=nombre_colegio)

                    # Crear el mensaje
                    mensaje = MIMEMultipart()
                    mensaje["From"] = EMAIL_CONFIG_MARKETING["USER"]
                    mensaje["To"] = email_contacto
                    mensaje["Subject"] = f"Promoción Especial para {nombre_colegio}"
                    mensaje.attach(MIMEText(html, "html", _charset="utf-8"))
                    mensaje.attach(logo)

                    # Enviar el correo
                    servidor.sendmail(EMAIL_CONFIG_MARKETING["USER"], email_contacto, mensaje.as_string())
                    print(f"Correo enviado a {nombre_colegio} ({email_contacto})")

    except FileNotFoundError as file_error:
        print(f"Archivo no encontrado: {file_error}")
    except smtplib.SMTPException as smtp_error:
        print(f"Error SMTP al enviar correos: {smtp_error}")
    except Exception as e:
        print(f"Error inesperado al enviar correos: {e}")
    finally:
        print("Proceso de envío completado.")


