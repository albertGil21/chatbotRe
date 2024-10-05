from flask import Flask, request, jsonify
from flask_cors import CORS
from main import GeminiChatManager
import uuid

app = Flask(__name__)
CORS(app)

# Crear una instancia del manejador de chat
chat_manager = GeminiChatManager()

@app.route('/', methods=['GET'])
def home():
    return 'API is running!'

@app.route('/api/new-session', methods=['POST'])
def new_session():
    """Crear una nueva sesión de chat."""
    session_id = str(uuid.uuid4())
    created = chat_manager.create_new_session(session_id)
    if created:
        return jsonify({
            'session_id': session_id,
            'message': 'Nueva sesión creada exitosamente'
        }), 200
    return jsonify({'error': 'No se pudo crear la sesión'}), 400

@app.route('/api/ask', methods=['POST'])
def ask():
    """Enviar un mensaje a una sesión específica."""
    data = request.json
    session_id = data.get('session_id')
    message = data.get('message')
    
    if not session_id or not message:
        return jsonify({
            'error': 'Se requiere session_id y message'
        }), 400
    
    response_text = chat_manager.send_message(session_id, message)
    return jsonify({
        'response': response_text,
        'session_id': session_id
    }), 200

@app.route('/api/end-session', methods=['POST'])
def end_session():
    """Finalizar una sesión de chat."""
    session_id = request.json.get('session_id')
    if session_id and chat_manager.delete_session(session_id):
        return jsonify({
            'message': 'Sesión finalizada exitosamente'
        }), 200
    return jsonify({
        'error': 'No se pudo finalizar la sesión'
    }), 400

if __name__ == '__main__':
    app.run()