from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Cargar respuestas desde JSON
def load_responses():
    try:
        with open('respuestas.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("❌ Error: No se encontró el archivo responses.json")
        return {}
    except json.JSONDecodeError:
        print("❌ Error: El archivo responses.json tiene formato incorrecto")
        return {}

def chatbot_response(user_message):
    responses = load_responses()
    user_message = user_message.lower().strip()
    
    # Buscar coincidencia en las respuestas
    for category, data in responses.items():
        if category == "default":
            continue
            
        keywords = data.get("keywords", [])
        for keyword in keywords:
            if keyword in user_message:
                return data.get("response", "Lo siento, no tengo una respuesta para eso.")
    
    # Respuesta por defecto si no hay coincidencias
    default_response = responses.get("default", {}).get("response", "No tengo una respuesta para eso en este momento.")
    return default_response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        if not request.is_json:
            return jsonify({'response': 'Error: Se esperaba JSON'}), 400
        
        user_message = request.json.get('message')
        
        if not user_message:
            return jsonify({'response': 'No recibí ningún mensaje'}), 400
        
        response = chatbot_response(user_message)
        return jsonify({'response': response})
        
    except Exception as e:
        print(f"❌ Error en el servidor: {e}")
        return jsonify({'response': 'Error interno del servidor'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)