from flask import Flask

# Criação do objeto Flask
app = Flask(__name__)

# Rota principal (home)
@app.route('/')
def home():
    return 'Hello, World!'

# Verifica se o script está sendo executado diretamente e roda o servidor
if __name__ == '__main__':
    app.run(debug=True)
