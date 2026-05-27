from app import app
from flask import render_template

@app.route("/")
def home():
    dados = {
        'nome': 'Kaio',
        'produtos': ['Banana', 'Abacaxi', 'Melancia']
    }
    logado = True
    return render_template("index.html", pessoa = dados, usuario_logado = logado)

@app.route("/sobre")
def sobre():
    return "Página Sobre"

@app.route("/endereço")
def endereco():
    return "Rua Presidente Getúlio Vargas, 576"

@app.route("/preferidos")
def preferidos():
    return """<h1>Hobbies</h1>
    <ul>
        <li>RPG</li>
        <li>Escutar música</li>
        <li>Jogar</li>
    </ul>"""

@app.route("/contatos")
def contatos():
    return """<h1>Contatos</h1>
    <ul>
        <li>Whatsapp: +55 84 99865-9580</li>
        <li>Instagram: @Wolyo_Wolf</li>
        <li>Discord: LobinWolyo</li>
    </ul>"""