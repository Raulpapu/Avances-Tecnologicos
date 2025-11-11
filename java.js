async function sendMessage() {
    const userInput = document.getElementById('userInput');
    const message = userInput.value.trim();
    
    if (message === '') return;
    
    console.log("🔵 Enviando mensaje:", message);
    
    // Mostrar mensaje del usuario
    displayMessage(message, 'user');
    userInput.value = '';
    
    // Mostrar indicador de typing
    showTypingIndicator();
    
    try {
        const response = await fetch('http://127.0.0.1:5000/get_response', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });
        
        // Ocultar indicador de typing
        hideTypingIndicator();
        
        console.log(" Respuesta recibida. Status:", response.status);
        
        if (!response.ok) {
            throw new Error(`Error del servidor: ${response.status}`);
        }
        
        const data = await response.json();
        console.log(" Datos recibidos");
        displayMessage(data.response, 'bot');
        
    } catch (error) {
        // Ocultar indicador de typing en caso de error
        hideTypingIndicator();
        
        console.error(' Error completo:', error);
        displayMessage(' No se pudo conectar con el servidor. Verifica que esté ejecutándose en http://127.0.0.1:5000', 'bot');
    }
}

function displayMessage(message, sender) {
    const chatBox = document.getElementById('chatBox');
    const messageDiv = document.createElement('div');
    messageDiv.className = sender + '-message';
    
    // Mantener saltos de línea y formato
    messageDiv.innerHTML = message.replace(/\n/g, '<br>');
    
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function showTypingIndicator() {
    const chatBox = document.getElementById('chatBox');
    const typingDiv = document.createElement('div');
    typingDiv.id = 'typingIndicator';
    typingDiv.className = 'bot-message typing';
    typingDiv.innerHTML = '✈️ TravelBot está escribiendo...';
    
    chatBox.appendChild(typingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function hideTypingIndicator() {
    const typingIndicator = document.getElementById('typingIndicator');
    if (typingIndicator) {
        typingIndicator.remove();
    }
}

function insertSuggestion(suggestion) {
    document.getElementById('userInput').value = suggestion;
    document.getElementById('userInput').focus();
}

function handleKeyPress(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
}

// Verificar al cargar la página
document.addEventListener('DOMContentLoaded', function() {
    console.log("🟡 Página cargada. TravelBot con Gemini AI");
    console.log("🔗 Servidor: http://127.0.0.1:5000");
    document.getElementById('userInput').focus();
});