from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email
from app.models import Paciente


class PacienteForm(FlaskForm):
    nome_completo = StringField(
        "Nome completo",
        validators=[
            DataRequired(message="O nome completo é obrigatório."),
            Length(max=150, message="O nome completo deve ter até 150 caracteres."),
        ],
    )
    username = StringField(
        "Username",
        validators=[
            DataRequired(message="O username é obrigatório."),
            Length(max=80, message="O username deve ter até 80 caracteres."),
        ],
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="O email é obrigatório."),
            Length(max=120, message="O email deve ter até 120 caracteres."),
            Email(message="Informe um email válido."),
        ],
    )
    submit = SubmitField("Cadastrar")
    
    
    def validate_username(self, field):
        pacientes = Paciente.all()
        for paciente in pacientes:
            if paciente.username == field.data:
                raise ValidationError("Este username já está em uso. Por favor, escolha outro.")
            
            
    def validate_email(self, field):
        pacientes = Paciente.all()
        for paciente in pacientes:
            if paciente.email == field.data:
                raise ValidationError("Este email já está em uso. Por favor, escolha outro.")


    def to_dict(self):
        return {
            "nome_completo": self.nome_completo.data,
            "username": self.username.data,
            "email": self.email.data,
        }
