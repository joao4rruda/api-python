from flask import Flask, jsonify
from flask_cors import CORS  # Importação para permitir CORS
from db import items  # Certifique-se de que `db.py` contém a lista `items`

# Inicialização do Flask
app = Flask(__name__)
CORS(app)  # Habilita CORS para evitar problemas com requisições externas

# Rota principal (home)
@app.route('/', methods=["GET"])
def home():
    return jsonify({"message": "Bem-vindo à API!"})

# Rota para obter a lista de itens
@app.route('/items', methods=["GET"])
def get_items():
    return jsonify(items), 200  # Retorna os itens com status HTTP 200

# Rota de status
@app.route('/status', methods=["GET"])
def status():
    return jsonify({"status": "running", "version": "1.0.0"}), 200

# Rota de erro para páginas inexistentes
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Not Found",
        "message": "A rota que você tentou acessar não existe."
    }), 404

# Inicialização do servidor Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
