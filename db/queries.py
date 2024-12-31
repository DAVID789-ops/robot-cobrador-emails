from db.connection import get_connection

def obtener_deudas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_colegio, cantidad_deuda, producto_entregado, fecha_entrega, email_contacto, signo, intensidad, idioma, tiempo FROM deudas")
    registros = cursor.fetchall()
    conn.close()
    return registros
