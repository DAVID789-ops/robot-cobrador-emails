from db.connection import get_connection

def obtener_marketing():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_colegio, email_contacto, idioma, email_marketing FROM deudas")
    registros = cursor.fetchall()
    conn.close()
    return registros