import json

class DataStorage:
    def save_to_json(self, file_path, entities):
        data = []

        for entity in entities:
            data.append(entity.to_dict())

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

    def load_from_json(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
