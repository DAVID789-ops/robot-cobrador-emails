from db.queries import obtener_deudas
from emails.send_email import enviar_correos

if __name__ == "__main__":
    try:
        deudas = obtener_deudas()
        enviar_correos(deudas)
    except Exception as e:
        print(f"Error general: {e}")
