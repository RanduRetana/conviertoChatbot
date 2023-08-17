import mysql.connector as mysql

# create connection to database
def create_conn():
    conn = mysql.connect(
        host="35.211.5.248",
        port=3306,
        user="bn_wordpress",
        passwd="36721bad982d385527779574aa80a9cdb2f27fb31f03d851f38b028bec837570",
        database="bitnami_wordpress"
    )
    return conn

def save_user_data(session_id, name, contact):
    # user_id, _ = session_id.split("_")
    apellido = "Apellido predeterminado"
    correo = contact
    titulo = "Título predeterminado"

    conn = create_conn()
    cursor = conn.cursor()

    query_posts = """
    INSERT INTO wp_posts (post_author, post_date, post_date_gmt, post_content, post_title, post_excerpt, post_status, post_type, to_ping, pinged, post_modified, post_modified_gmt, post_content_filtered)
    VALUES (%s, NOW(), NOW(), %s, %s, '', 'publish', 'prospectos', '', '', NOW(), NOW(), '')
    """
    values_posts = (session_id, "prueba", titulo)
    cursor.execute(query_posts, values_posts)
    conn.commit()

    post_id = cursor.lastrowid

    query_postmeta = "INSERT INTO wp_postmeta (post_id, meta_key, meta_value) VALUES (%s, %s, %s)"

    values_nombre = (post_id, "nombre", name)
    cursor.execute(query_postmeta, values_nombre)

    values_apellido = (post_id, "apellido", apellido)
    cursor.execute(query_postmeta, values_apellido)

    values_correo = (post_id, "correo", correo)
    cursor.execute(query_postmeta, values_correo)

    conn.commit()
    cursor.close()
    conn.close()


#the following function returns the user_url using the id given
def get_user_url(id):
    conn = create_conn()
    cursor = conn.cursor()

    query = """ select meta_value from wp_usermeta where user_id = %s and meta_key = "billing_company" """
    values = (id,)

    cursor.execute(query, values)
    result = cursor.fetchone()
    user_url = result[0] if result is not None else "tu empresa favorita"

    cursor.close()
    conn.close()

    return user_url


