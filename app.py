from flask import Flask, jsonify
from db import items

# Criação do objeto Flask
app = Flask(__name__)

# Rota principal (home)
@app.route('/', methods="GET")
def home():
    return jsonify({
        items
    })

# Rota de status
@app.route('/status')
def status():
    return jsonify({"status": "running", "version": "1.0.0"})

# Rota de erro para lidar com páginas inexistentes
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found", "message": "Rota não encontrada"}), 404

# Verifica se o script está sendo executado diretamente e roda o servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)