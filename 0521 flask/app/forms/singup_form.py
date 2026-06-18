from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField 

from wtforms.validators import DataRequired, EqualTo, Email

class SingupForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(message='Por favor, preencha o seu nome.')])
    email = EmailField('Email', validators=[Email(message='Insira um email válido.'), DataRequired(message='Por favor, preencha o email.')])
    password = PasswordField('Senha', [DataRequired(message='Por favor, preencha a senha.'), EqualTo('confirm', message='As senhas devem ser iguais.')])
    confirm  = PasswordField('Confirme a senha')
    submit = SubmitField('Cadastrar-se')