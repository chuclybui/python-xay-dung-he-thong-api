import requests
from user import User
from post import Post


class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_users(self, limit):
        response = requests.get(f"{self.BASE_URL}/users")
        response.raise_for_status()

        data = response.json()

        users = []

        for item in data[:limit]:
            user = User(
                id=item["id"],
                name=item["name"],                
                email=item["email"]
            )

            users.append(user)

        return users

    def get_posts(self, limit):
        response = requests.get(f"{self.BASE_URL}/posts")
        response.raise_for_status()

        data = response.json()

        posts = []

        for item in data[:limit]:
            post = Post(                
                id=item["id"],
                title=item["title"],
                body=item["body"]
            )

            posts.append(post)

        return posts
    
        