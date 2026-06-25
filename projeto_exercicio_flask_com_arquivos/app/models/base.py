import datetime

from app.storage import storage


class ValidationError(ValueError):
    pass


class JSONModel:
    collection = None
    fields = ()
    required_fields = ()
    unique_fields = ()

    def __init__(self, **data):
        for field in ("id", *self.fields, "criado_em"):
            setattr(self, field, data.get(field))

    def to_dict(self):
        return {
            field: getattr(self, field)
            for field in ("id", *self.fields, "criado_em")
            if getattr(self, field, None) is not None
        }

    @classmethod
    def all(cls):
        return [cls(**item) for item in storage.all(cls.collection)]

    @classmethod
    def get(cls, item_id):
        item = storage.get(cls.collection, item_id)
        if item is None:
            return None
        return cls(**item)

    @classmethod
    def create(cls, data):
        data = cls._clean_data(data)
        data["criado_em"] = cls._now()
        cls._validate(data)
        cls._validate_unique(data)
        return cls(**storage.create(cls.collection, data))

    @classmethod
    def update(cls, item_id, data):
        existing = storage.get(cls.collection, item_id)
        if existing is None:
            return None

        changes = cls._clean_data(data, partial=True)
        updated = {**existing, **changes}
        cls._validate(updated)
        cls._validate_unique(updated, current_id=int(item_id))
        return cls(**storage.update(cls.collection, item_id, changes))

    @classmethod
    def delete(cls, item_id):
        return storage.delete(cls.collection, item_id)

    @classmethod
    def _clean_data(cls, data, partial=False):
        if not isinstance(data, dict):
            raise ValidationError("O corpo da requisição deve ser um objeto JSON.")

        allowed_fields = set(cls.fields)
        unknown_fields = set(data) - allowed_fields
        if unknown_fields:
            fields = ", ".join(sorted(unknown_fields))
            raise ValidationError(f"Campos desconhecidos: {fields}.")

        cleaned = {}
        for field in cls.fields:
            if field in data:
                cleaned[field] = data[field]

        if not partial:
            for field in cls.required_fields:
                cleaned.setdefault(field, None)

        return cls._normalize(cleaned)

    @classmethod
    def _normalize(cls, data):
        return data

    @classmethod
    def _validate(cls, data):
        missing_fields = [
            field
            for field in cls.required_fields
            if data.get(field) in (None, "")
        ]
        if missing_fields:
            fields = ", ".join(missing_fields)
            raise ValidationError(f"Campos obrigatórios ausentes: {fields}.")

    @classmethod
    def _validate_unique(cls, data, current_id=None):
        for field in cls.unique_fields:
            value = data.get(field)
            for item in storage.all(cls.collection):
                same_item = current_id is not None and item["id"] == current_id
                if item.get(field) == value and not same_item:
                    raise ValidationError(f"Já existe registro com {field}={value}.")

    @staticmethod
    def _now():
        return datetime.datetime.utcnow().replace(microsecond=0).isoformat()
