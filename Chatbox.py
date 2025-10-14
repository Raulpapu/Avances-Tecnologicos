from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def chatbot_response(user_message):
    user_message = user_message.lower().strip()
    
    # SALUDOS MEJORADOS
    if any(palabra in user_message for palabra in ["hola", "buenos dias", "buenas tardes", "buenas noches"]):
        return "¡Hola! 🌍 Soy **TravelBot**, tu experto en destinos turísticos.\n\nPuedo recomendarte:\n• Lugares por continente\n• Playas paradisíacas\n• Ciudades históricas\n• Aventuras extremas\n• Destinos exóticos\n\n¿Por dónde quieres empezar tu viaje soñado? ✈️"

    # EUROPA MEJORADA
    elif "europa" in user_message:
        return "🌍 **EUROPA - Continente de Historia y Cultura**\n\n🏛️ **Cultural:**\n• **Roma, Italia** - Coliseo, Vaticano y pasta auténtica\n• **Atenas, Grecia** - Acrópolis y ruinas antiguas\n• **París, Francia** - Torre Eiffel y museos mundialmente famosos\n\n🏔️ **Naturaleza:**\n• **Alpes Suizos** - Montañas espectaculares y lagos cristalinos\n• **Fiordos Noruegos** - Paisajes glaciares únicos\n• **Costa Amalfitana** - Pueblos coloridos sobre el mar\n\n🏰 **Ciudades Mágicas:**\n• **Praga** - Arquitectura gótica y barroca\n• **Barcelona** - Obras de Gaudí y playas urbanas\n• **Londres** - Palacios reales y cultura vibrante\n\n¿Te interesa algún país específico?"

    # ASIA MEJORADA
    elif "asia" in user_message:
        return "🌏 **ASIA - Donde lo Ancestral Encuentra lo Moderno**\n\n🏯 **Tradicional:**\n• **Kioto, Japón** - Templos milenarios y geishas\n• **Angkor Wat, Camboya** - Complejo arqueológico impresionante\n• **Taj Mahal, India** - Monumento al amor eterno\n\n🏝️ **Paraíso Tropical:**\n• **Bali, Indonesia** - Arrozales, templos y playas de ensueño\n• **Maldivas** - Bungalows sobre aguas turquesa\n• **Phi Phi Islands, Tailandia** - Escenario de 'La Playa'\n\n🏙️ **Modernidad:**\n• **Tokio, Japón** - Tecnología y tradición fusionadas\n• **Singapur** - Ciudad futurista y jardines verticales\n• **Seúl, Corea** - K-pop, templos y gastronomía única\n\n¿Buscas aventura, relax o cultura?"

    # AMÉRICA MEJORADA
    elif "america" in user_message:
        return "🌎 **AMÉRICA - De lo Salvaje a lo Cosmopolita**\n\n🗿 **Antiguas Civilizaciones:**\n• **Machu Picchu, Perú** - Ciudadela inca en las nubes\n• **Chichén Itzá, México** - Pirámide maya y cenotes\n• **Tikal, Guatemala** - Ruinas mayas en la jungla\n\n🏞️ **Maravillas Naturales:**\n• **Cataratas del Iguazú** - 275 saltos entre Argentina y Brasil\n• **Gran Cañón, USA** - Cañón monumental de colores\n• **Amazonas** - Pulmón del planeta y biodiversidad única\n\n🌆 **Ciudades Vibrantes:**\n• **Nueva York** - Rascacielos, Broadway y cultura\n• **Río de Janeiro** - Cristo Redentor y carnaval\n• **Cartagena, Colombia** - Ciudad amurallada y Caribe\n\n¿Norte, Centro o Sur América?"

    # PLAYAS MEJORADAS
    elif any(palabra in user_message for palabra in ["playa", "playas", "mar", "arena"]):
        return "🏖️ **PLAYAS PARADISÍACAS DEL MUNDO**\n\n💎 **Lujo y Exclusividad:**\n• **Bora Bora, Polinesia** - Bungalows sobre aguas cristalinas\n• **Maldivas** - Arenas blancas y arrecifes de coral\n• **Seychelles** - Rocas graníticas y aguas transparentes\n\n🌴 **Tropical y Vibrante:**\n• **Cancún, México** - Aguas turquesa y vida nocturna\n• **Phuket, Tailandia** - Calas escondidas y cultura tailandesa\n• **Hawái, USA** - Volcanes, surf y tradiciones polinesias\n\n🌅 **Exóticas y Únicas:**\n• **Whitehaven Beach, Australia** - Arena de sílice puro\n• **Fernando de Noronha, Brasil** - Reserva natural protegida\n• **Zanzíbar, Tanzania** - Cultura swahili y especias\n\n¿Prefieres lujo, aventura o tranquilidad?"

    # MONTAÑAS MEJORADAS
    elif any(palabra in user_message for palabra in ["montaña", "montañas", "senderismo", "trekking"]):
        return "⛰️ **DESTINOS DE MONTAÑA Y AVENTURA**\n\n🏔️ **Alturas Extremas:**\n• **Monte Everest, Nepal** - Campo base para los más aventureros\n• **Alpes Suizos** - Esquí, snowboard y pueblos alpinos\n• **Patagonia** - Torres del Paine y glaciares milenarios\n\n🥾 **Trekking y Naturaleza:**\n• **Inca Trail, Perú** - Camino a Machu Picchu (4 días)\n• **Parque Nacional Banff, Canadá** - Lagos esmeralda y vida silvestre\n• **Himalaya, India** - Monasterios budistas y paisajes épicos\n\n🌄 **Paisajes Únicos:**\n• **Cappadocia, Turquía** - Vuelos en globo sobre chimeneas de hadas\n• **Zhangjiajie, China** - Montañas que inspiraron 'Avatar'\n• **Fiordos Noruegos** - Cruceros entre montañas y cascadas\n\n¿Buscas desafío extremo o paisajes fotogénicos?"

    # LUGARES EXÓTICOS MEJORADOS
    elif any(palabra in user_message for palabra in ["exótico", "exotico", "raro", "único", "unico"]):
        return "🌟 **DESTINOS EXÓTICOS QUE PARECEN DE OTRO PLANETA**\n\n🎨 **Naturalmente Extraordinarios:**\n• **Salar de Uyuni, Bolivia** - El espejo natural más grande del mundo\n• **Isla de Pascua, Chile** - Moais gigantes en medio del Pacífico\n• **Pamukkale, Turquía** - Termas blancas como algodón\n\n🏜️ **Desiertos y Formaciones Únicas:**\n• **Desierto de Wadi Rum, Jordania** - Paisajes marcianos (filmación de 'The Martian')\n• **Zhangye Danxia, China** - Montañas arcoíris de colores\n• **Caño Cristales, Colombia** - 'Río de los cinco colores'\n\n🌌 **Fenómenos Naturales:**\n• **Aurora Boreal** - Luces del norte en Islandia/Noruega\n• **Cuevas Waitomo, Nueva Zelanda** - Cuevas iluminadas por luciérnagas\n• **Lago Hillier, Australia** - Lago de color rosa chicle\n\n¿Te atraen los colores únicos, formaciones extrañas o fenómenos naturales?"

    # CONSEJOS MEJORADOS
    elif any(palabra in user_message for palabra in ["consejo", "recomendacion", "tip", "viajar"]):
        return "💡 **CONSEJOS DE VIAJERO EXPERTO**\n\n📋 **Planificación:**\n• Investica requisitos de visa y vacunas con 3 meses de anticipación\n• Lleva seguro de viaje que cubra actividades de aventura\n• Haz copias digitales de tus documentos importantes\n\n🎒 **Equipaje Inteligente:**\n• Lleva efectivo local y tarjetas internacionales\n• Incluye botiquín básico y medicamentos personales\n• Ropa versátil que se pueda usar en capas\n\n🌍 **Durante el Viaje:**\n• Respeta costumbres y vestimenta local\n• Aprende frases básicas en el idioma local\n• Prueba la comida callejera (en lugares con buena higiene)\n• Mantén mente abierta y sé flexible con los planes\n\n📱 **Tecnología:**\n• Descarga mapas offline antes de salir\n• Usa aplicaciones de traducción instantánea\n• Comparte tu itinerario con familiares\n\n¡El mejor recuerdo es una experiencia segura y memorable!"

    # RESPUESTA POR DEFECTO MEJORADA
    else:
        return "✈️ **¡Excelente pregunta!** Como tu guía turístico personal, puedo ayudarte a descubrir:\n\n🌎 **Por Continente:** Europa, Asia, América, África, Oceanía\n🏖️ **Por Tipo:** Playas, montañas, ciudades, aventura, relax\n🌟 **Especiales:** Lugares exóticos, maravillas naturales, culturas únicas\n💡 **Consejos:** Planificación, equipaje, seguridad cultural\n\nTambién puedo recomendarte países específicos como:\n• México, España, Japón, Tailandia, Italia, etc.\n\n¿Qué tipo de experiencia de viaje estás buscando?"

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