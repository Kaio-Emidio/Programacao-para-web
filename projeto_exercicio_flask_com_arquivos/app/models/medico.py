from app.models.base import JSONModel, ValidationError
from app.storage import storage


class Medico(JSONModel):
    collection = "medicos"
    fields = ("nome_completo", "crm", "especialidade")
    required_fields = fields
    unique_fields = ("crm",)

    @classmethod
    def _normalize(cls, data):
        if "crm" in data and data["crm"] not in (None, ""):
            try:
                data["crm"] = int(data["crm"])
            except (TypeError, ValueError) as error:
                raise ValidationError("O campo crm deve ser um número inteiro.") from error
        return data

    @classmethod
    def delete(cls, item_id):
        item = storage.get(cls.collection, item_id)
        if item is None:
            return False

        for consulta in storage.all("consultas"):
            if consulta["id_medico"] == int(item_id):
                raise ValidationError(
                    "Não é possível excluir médico com consulta cadastrada."
                )

        return super().delete(item_id)
