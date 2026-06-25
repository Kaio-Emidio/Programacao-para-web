from app.models.base import JSONModel, ValidationError
from app.storage import storage


class Consulta(JSONModel):
    collection = "consultas"
    fields = ("id_medico", "id_paciente", "data_hora_marcada")
    required_fields = fields

    @classmethod
    def _normalize(cls, data):
        for field in ("id_medico", "id_paciente"):
            if field in data and data[field] not in (None, ""):
                try:
                    data[field] = int(data[field])
                except (TypeError, ValueError) as error:
                    raise ValidationError(
                        f"O campo {field} deve ser um número inteiro."
                    ) from error
        return data

    @classmethod
    def _validate(cls, data):
        super()._validate(data)

        if storage.get("medicos", data["id_medico"]) is None:
            raise ValidationError("O médico informado não existe.")

        if storage.get("pacientes", data["id_paciente"]) is None:
            raise ValidationError("O paciente informado não existe.")
