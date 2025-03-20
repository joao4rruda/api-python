from flask import Flask, jsonify
from flask_cors import CORS
from db import db  # Importando a instância `db` de `db.py`

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Bem-vindo à API!"})

@app.route("/nota-fiscal-entrada-item", methods=["GET"])
def get_items():
    try:
        items = db.get_NotaFiscalEntradaItem()  # Obtém os dados do banco
        return jsonify(items), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "running", "version": "1.0.0"}), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Not Found",
        "message": "A rota que você tentou acessar não existe."
    }), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
