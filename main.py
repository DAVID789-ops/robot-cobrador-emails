from db.queries import obtener_deudas
from db.queries_marketing import obtener_marketing as obtener_marketing
from emails.español_send_email import enviar_correos as enviar_correos_es
from emails.ingles_send_email import enviar_correos as enviar_correos_en
from emails.frances_send_email import enviar_correos as enviar_correos_fr
from emails.email_marketing.marketing_español import enviar_correos as enviar_correos_marketing  
from emails.email_marketing.marketing_ingles import enviar_correos as enviar_correos_marketing_en  
from emails.email_marketing.marketing_frances import enviar_correos as enviar_correos_marketing_fr

if __name__ == "__main__":
    try:
        deudas = obtener_deudas()

        #Enviar correos en español
        enviar_correos_es(deudas)

        #Enviar correos en inglés
        enviar_correos_en(deudas)

        #Enviar correos en frances
        enviar_correos_fr(deudas)

        #Enviar correos de marketing español
        marketing = obtener_marketing()
        enviar_correos_marketing(marketing)

        #Enviar correos de marketing en inglés
        marketing = obtener_marketing()
        enviar_correos_marketing_en(marketing)

        #Enviar correos de marketing en frances
        marketing = obtener_marketing()
        enviar_correos_marketing_fr(marketing)
        
    except Exception as e:
        print(f"Error general: {e}")
