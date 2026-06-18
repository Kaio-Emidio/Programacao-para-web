from app import app
from flask import render_template, redirect, flash
from app.forms.login_form import LoginForm
from app.forms.singup_form import SingupForm
from app.controllers.AuthenticationController import AuthenticationController

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

@app.route('/login', methods = ['GET', 'POST'])
def login():
    formulario = LoginForm()
    if formulario.validate_on_submit():
        if AuthenticationController.login(formulario):
            flash('Login efetuado com sucesso.')
            return redirect('/')
        else:
            flash("Erro nas credenciais.")
            return redirect('/login')
    return render_template('login.html', title = 'Login', form = formulario)

@app.route('/cadastro', methods = ['GET', 'POST'])
def cadastro():
    formulario = SingupForm()
    if formulario.validate_on_submit():
        if AuthenticationController.singup(formulario):
            flash('Cadastro realizado com sucesso')
            return redirect('/')
        else: 
            flash('Erro nas credenciais')
            return redirect('/cadastro')
    return render_template('singup.html', title = 'Cadastro', form = formulario)