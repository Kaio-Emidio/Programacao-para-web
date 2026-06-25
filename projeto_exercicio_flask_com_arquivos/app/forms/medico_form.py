from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, EmailField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email
from app.models import Medico

class MedicoForm(FlaskForm):
    nome_completo = StringField('Nome Completo', [DataRequired(), Length(min=5, max=100)])
    username = StringField('Nome de Usuário', [DataRequired(), Length(min=5, max=100)])
    crm = StringField("CRM", [DataRequired(), Length(min=8, max=8)])
    especialidade = SelectField("Especialidade", [DataRequired()], choices=[
        ('card', 'Cardiologia'), 
        ('derm', 'Dermatologia'), 
        ('gine', 'Ginecologia'), 
        ('neur', 'Neurologia'), 
        ('orto', 'Ortopedia'), 
        ('pedi', 'Pediatria'), 
        ('psiq', "Psiquiatria"), 
        ('urol', "Urologia"), 
        ('ofta', "Oftalmologia"), 
        ('otor', "Otorrinolaringologia"), 
        ('endo', "Endocrinologia"), 
        ('gast', "Gastroenterologia"), 
        ('pneu', 'Pneumologia'), 
        ('reum', 'Reumatologia'), 
        ('onco', 'Oncologia'), 
        ('radi', 'Radiologia'), 
        ('anes', 'Anestesiologia'), 
        ('CirG', 'Cirurgia Geral'), 
        ('medI','Medicina Interna'), 
        ('medF', 'Medicina de Família')
    ])
    email = EmailField('Email', [DataRequired(), Email()])
    submit = SubmitField('Cadastrar Médico')

    def validate_username(self, field):
        medicos = Medico.all()
        for medico in medicos:
            if medico.username == field.data:
                raise ValidationError("Esse nome de usuário já está sendo utilizado, esolha outro.")