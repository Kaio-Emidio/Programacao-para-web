from collections.abc import Sequence
from typing import Any, Mapping
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, ValidationError

from wtforms.validators import DataRequired, EqualTo, Email

class SingupForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(message='Por favor, preencha o seu nome.')])
    email = EmailField('Email', validators=[Email(message='Insira um email válido.'), DataRequired(message='Por favor, preencha o email.')])
    password = PasswordField('Senha', validators=[DataRequired(message='Por favor, preencha a senha.'), EqualTo('confirm', message='As senhas devem ser iguais.')])
    confirm  = PasswordField('Confirme a senha', validators=[DataRequired(message='Por favor, preencha a confirmação da senha.'), EqualTo('password', message='As senhas devem ser iguais.')])
    submit = SubmitField('Cadastrar-se')
    
    def validate_username(self, field):
        if field.data.lower() == 'admin':
            raise ValidationError('O nome "admin" está reservado. Escolha outro.')
        
    def validate_password(self, field):
        if field.data.lower() == '123456':
            raise ValidationError('A senha é muito simples. Crie uma mais forte.')