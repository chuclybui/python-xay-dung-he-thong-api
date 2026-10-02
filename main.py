import json
from apiClient import APIClient
from dataStorage import DataStorage

if __name__ == "__main__": 
  try:
    api_client = APIClient()
 
    users = api_client.get_users(5)
    
    posts = api_client.get_posts(5)

   
    all_data = users + posts

    storage = DataStorage()

    storage.save_to_json(
        "system_data.json",
        all_data
    )
    
    loaded_data = storage.load_from_json(
        "system_data.json"
    )
    
    print(
        json.dumps(
            loaded_data,
            indent=4,
            ensure_ascii=False
        )
    )
  except (TypeError, ValueError) as error:
    print(f"Lỗi dữ liệu: {error}")