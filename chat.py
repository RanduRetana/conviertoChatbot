import random
import json
from database import save_user_data, get_user_url


chat_state = "initial"
user_data = {}


awaiting_name_email = False

chat_state = {}  # Cambiar a un diccionario


def get_response(sentence, session_id, bot_name, saludo, despedida, is_welcome_message, usuario):
    global chat_state, user_data

    user_url = get_user_url(usuario)
    if session_id not in chat_state:
        chat_state[session_id] = "initial"

    if is_welcome_message:
        response = saludo
        chat_state[session_id] = "awaiting_assistance"
    elif chat_state[session_id] == "awaiting_assistance":
        # Código para manejar la respuesta del usuario
        response = f"Te voy a asignar un asesor, dame tu nombre por favor."
        chat_state[session_id] = "awaiting_name"
    elif chat_state[session_id] == "awaiting_name":
        user_data["name"] = sentence
        response = "Ahora dame tu correo o WhatsApp."
        chat_state[session_id] = "awaiting_contact"
    elif chat_state[session_id] == "awaiting_contact":
        user_data["contact"] = sentence
        # Guardar nombre y contacto en la base de datos
        save_user_data(usuario, user_data["name"], user_data["contact"])
        response = despedida
        chat_state[session_id] = "finalizado"
    # else:
    #     response = "No entiendo..."
    if chat_state[session_id] == "finalizado":
        response = despedida
        chat_state[session_id] = "fin"


    return response


