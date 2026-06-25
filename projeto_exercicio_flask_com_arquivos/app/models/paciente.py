from app.models.base import JSONModel, ValidationError
from app.storage import storage


class Paciente(JSONModel):
    collection = "pacientes"
    fields = ("nome_completo", "username", "email")
    required_fields = fields
    unique_fields = ("username", "email")

    @classmethod
    def delete(cls, item_id):
        item = storage.get(cls.collection, item_id)
        if item is None:
            return False

        for consulta in storage.all("consultas"):
            if consulta["id_paciente"] == int(item_id):
                raise ValidationError(
                    "Não é possível excluir paciente com consulta cadastrada."
                )

        return super().delete(item_id)
