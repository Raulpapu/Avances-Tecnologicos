import google.generativeai as genai

# PEGA TU API KEY AQUÍ
API_KEY = "AIzaSyBdOEsKZoAWwRsHNJ18vbRIXy0OumLLw3c"

print("🧪 TEST FINAL DE GEMINI")
print(f"Key: {API_KEY[:20]}...")
print(f"Longitud: {len(API_KEY)}")

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Responde 'FUNCIONA' si todo está bien")
    print(f"✅ RESULTADO: {response.text}")
except Exception as e:
    print(f"❌ ERROR: {e}")