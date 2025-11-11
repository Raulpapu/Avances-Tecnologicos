from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai
import json
import os

app = Flask(__name__)
CORS(app)

# =============================================
# CONFIGURACIÓN DIRECTA Y SIMPLE
# =============================================

# Configuración DIRECTA de Gemini - SIN .env
GEMINI_API_KEY = "AIzaSyBdOEsKZoAWwRsHNJ18vbRIXy0OumLLw3c"  # ⚠️ REEMPLAZA ESTO CON TU API KEY REAL

print("🚀 INICIANDO TRAVELBOT CON GEMINI")
print(f"🔑 API Key: {GEMINI_API_KEY[:15]}...")

try:
    genai.configure(api_key=GEMINI_API_KEY)
    gemini_configured = True
    print("✅ GEMINI CONFIGURADO CORRECTAMENTE")
except Exception as e:
    print(f"❌ Error configurando Gemini: {e}")
    gemini_configured = False

# =============================================
# FUNCIONES PRINCIPALES
# =============================================

def get_gemini_response(user_message):
    """Obtener respuesta de Gemini - Versión Ultra Simple"""
    if not gemini_configured:
        return None
    
    try:
        print(f"🤖 Pregunta para Gemini: {user_message}")
        
        # Usar el modelo más básico y confiable
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""Eres TravelBot, un asistente de viajes experto. Responde esta pregunta sobre turismo: {user_message}
        
        Responde de manera útil, entusiasta y con información práctica. Usa emojis relevantes."""
        
        response = model.generate_content(prompt)
        print("✅ Respuesta de Gemini recibida")
        return response.text
        
    except Exception as e:
        print(f"❌ Error en Gemini: {e}")
        return None

def load_local_responses():
    """Cargar respuestas locales de emergencia"""
    try:
        with open('respuestas.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        return {}

def chatbot_response(user_message):
    """Generar respuesta - PRIORIDAD a Gemini"""
    print(f"📨 Mensaje recibido: {user_message}")
    
    # PRIMERO intentar con Gemini
    if gemini_configured:
        print("🎯 Intentando con Gemini...")
        gemini_response = get_gemini_response(user_message)
        if gemini_response:
            print("✅ Usando respuesta de Gemini")
            return gemini_response
        else:
            print("❌ Gemini falló, usando respuestas locales")
    
    # SEGUNDO: Respuestas locales como backup
    print("🔶 Usando respuestas locales")
    responses = load_local_responses()
    user_lower = user_message.lower()
    
    # Buscar coincidencia en respuestas locales
    for category, data in responses.items():
        if category == "default":
            continue
        for keyword in data.get("keywords", []):
            if keyword in user_lower:
                return data.get("response", "¡Hola! ¿En qué puedo ayudarte?")
    
    # Respuesta por defecto
    return "¡Hola! 🌍 Soy TravelBot. Puedo ayudarte con destinos turísticos, consejos de viaje y recomendaciones. ¿A dónde te gustaría viajar?"

# =============================================
# RUTAS FLASK
# =============================================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'response': 'No recibí ningún mensaje'}), 400
        
        response_text = chatbot_response(user_message)
        return jsonify({'response': response_text})
        
    except Exception as e:
        print(f"❌ Error en servidor: {e}")
        return jsonify({'response': 'Error temporal del servidor'}), 500

if __name__ == '__main__':
    print("\n" + "="*50)
    if gemini_configured:
        print("🎉 TRAVELBOT CON GEMINI AI - LISTO")
    else:
        print("🔶 TRAVELBOT MODO LOCAL - SIN GEMINI")
    print("🌐 http://127.0.0.1:5000")
    print("="*50)
    
    app.run(debug=True, host='127.0.0.1', port=5000)