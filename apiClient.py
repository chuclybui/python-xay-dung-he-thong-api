import requests
from user import User
from post import Post


class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __validate_limit(self, limit):
        if not isinstance(limit, int):
            raise TypeError("limit phải là số nguyên.")

        if limit <= 0:
            raise ValueError("limit phải lớn hơn 0.")
    def get_users(self, limit):
        self.__validate_limit(limit)
        
        try: 
          response = requests.get(f"{self.BASE_URL}/users", timeout=10)
          
          response.raise_for_status()

          data = response.json()
          
        except requests.RequestException as error:
            print(f"Lỗi khi gọi API users: {error}")
            return []

        except ValueError:
            print("Dữ liệu trả về từ API users không phải JSON hợp lệ.")
            return []

        users = [
            User(
                id=item["id"],
                name=item["name"],
                email=item["email"]
            )
            for item in data[:limit]
            if "id" in item
            and "name" in item
            and "email" in item
        ]

        return users

    def get_posts(self, limit):
        self.__validate_limit(limit)
        try:
            response = requests.get(f"{self.BASE_URL}/posts", timeout=10)
            
            response.raise_for_status()
            
            data = response.json()
            
        except requests.RequestException as error:
            print(f"Lỗi khi gọi API posts: {error}")
            return []
          
        except ValueError:
            print("Dữ liệu trả về từ API posts không phải JSON hợp lệ.")
            return []

        posts = [
            Post(
                id=item["id"],
                title=item["title"],
                body=item["body"]
            )
            for item in data[:limit]
            if "id" in item
            and "title" in item
            and "body" in item
        ]

        return posts
    
        