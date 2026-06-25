from app.models import Paciente


class PacienteController:
    def listar(self):
        return Paciente.all()

    def criar(self, data):
        return Paciente.create(data)
