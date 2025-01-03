from db.queries import obtener_deudas
from emails.español_send_email import enviar_correos as enviar_correos_es
from emails.ingles_send_email import enviar_correos as enviar_correos_en
from emails.frances_send_email import enviar_correos as enviar_correos_fr

if __name__ == "__main__":
    try:
        deudas = obtener_deudas()

        # Enviar correos en español
        enviar_correos_es(deudas)

        # Enviar correos en inglés
        enviar_correos_en(deudas)

        # Enviar correos en frances
        enviar_correos_fr(deudas)
        
    except Exception as e:
        print(f"Error general: {e}")
