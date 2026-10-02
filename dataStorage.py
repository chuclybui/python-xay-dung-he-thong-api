import json

from baseEntity import BaseEntity

class DataStorage:
    def save_to_json(self, file_path, entities):
        if not isinstance(file_path, str):
            raise TypeError("file_path phải là chuỗi.")

        if not file_path.strip():
            raise ValueError("file_path không được để trống.")

        if not isinstance(entities, list):
            raise TypeError("entities phải là một list.")

        # Validate tất cả phần tử
        if not all(
            isinstance(entity, BaseEntity)
            for entity in entities
        ):
            raise TypeError(
                "Tất cả phần tử trong entities phải kế thừa BaseEntity."
            )
            
        data = [
            entity.to_dict()
            for entity in entities
        ]
        
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(
                    data,
                    file,
                    indent=4,
                    ensure_ascii=False
                )
        except OSError as error:
           print(f"Lỗi khi ghi file: {error}")      

    def load_from_json(self, file_path):
        if not isinstance(file_path, str):
            raise TypeError("file_path phải là chuỗi.")

        if not file_path.strip():
            raise ValueError("file_path không được để trống.")
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {file_path} không tồn tại.")
            return []
        except json.JSONDecodeError:
            print(f"Dữ liệu trong file {file_path} không phải JSON hợp lệ.")
            return []
        except OSError as error:
            print(f"Lỗi khi đọc file: {error}")
            return []        
