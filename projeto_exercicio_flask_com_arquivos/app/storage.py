import json
import os

from flask import current_app, has_app_context

from config import Config


INITIAL_DATA = {
    "pacientes": [],
    "medicos": [],
    "consultas": [],
    "_next_ids": {
        "pacientes": 1,
        "medicos": 1,
        "consultas": 1,
    },
}


class JSONFileStorage:
    @property
    def path(self):
        if has_app_context():
            return current_app.config["JSON_STORAGE_FILE"]
        return Config.JSON_STORAGE_FILE

    def all(self, collection):
        data = self._read_data()
        return data[collection]

    def get(self, collection, item_id):
        item_id = int(item_id)
        data = self._read_data()

        for item in data[collection]:
            if item["id"] == item_id:
                return item

        return None

    def create(self, collection, item):
        data = self._read_data()

        item["id"] = data["_next_ids"][collection]
        data["_next_ids"][collection] += 1
        data[collection].append(item)

        self._write_data(data)
        return item

    def update(self, collection, item_id, changes):
        item_id = int(item_id)
        data = self._read_data()

        for item in data[collection]:
            if item["id"] == item_id:
                item.update(changes)
                item["id"] = item_id
                self._write_data(data)
                return item

        return None

    def delete(self, collection, item_id):
        item_id = int(item_id)
        data = self._read_data()

        for item in data[collection]:
            if item["id"] == item_id:
                data[collection].remove(item)
                self._write_data(data)
                return True

        return False

    def _read_data(self):
        self._create_file_if_needed()

        with open(self.path, encoding="utf-8") as file:
            return json.load(file)

    def _write_data(self, data):
        directory = os.path.dirname(self.path)
        os.makedirs(directory, exist_ok=True)

        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def _create_file_if_needed(self):
        if os.path.exists(self.path):
            return

        self._write_data(INITIAL_DATA)


storage = JSONFileStorage()
