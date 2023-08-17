from flask import send_from_directory
from flask import Flask, render_template, request, jsonify
from chat import get_response
from flask_cors import CORS
import uuid
import os

app = Flask(__name__)
CORS(app)


def generate_unique_id():
    return str(uuid.uuid4())


@app.route('/register_chatbot_user', methods=['POST'])
def register_chatbot_user():
    user_data = request.get_json()
    user_id = user_data.get("user_id")
    unique_id = generate_unique_id()
    combined_id = f"{user_id}_{unique_id}"
    # Guarda el ID combinado y los demás datos del usuario en la base de datos
    # ...
    return jsonify({"user_id": combined_id})



@app.get('/')
def index_get():
    return render_template('base.html')


@app.post('/predict')
def predict():
    data = request.get_json()
    text = data.get("message")
    user_id = data.get("user_id") 
    usuario = user_id.split("_")[0]
    bot_name = data.get("bot_name")
    saludo = data.get("saludo")
    despedida = data.get("despedida")
    response = get_response(text, user_id, bot_name, saludo, despedida, False, usuario)
    return jsonify({"response": response})

@app.route('/welcome_message', methods=['POST'])
def welcome_message():
    user_data = request.get_json()
    user_id = user_data.get("user_id")
    saludo = user_data.get("saludo")
    response = get_response(None, user_id, None, saludo, None, True, None)
    return jsonify({"response": response})


@app.route('/chatbot_loader.js')
def chatbot_loader():
    return send_from_directory('static', 'chatbot_loader.js')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), debug=True)

