from baseEntity import BaseEntity

class Post(BaseEntity):
    def __init__(self, id, title, body):
      super().__init__(id)
      if not isinstance(title, str):
            raise TypeError("title phải là chuỗi.")

      if not title.strip():
            raise ValueError("title không được để trống.")

      if not isinstance(body, str):
            raise TypeError("body phải là chuỗi.")

      if not body.strip():
            raise ValueError("body không được để trống.")

      self.__title = title.strip()
      self.__body = body.strip()

    @property
    def title(self):
      return self.__title
    
    @property
    def body(self):
      return self.__body
    
    def to_dict(self):
      return {
        "type": "Post",
        "id": self.id,
        "title": self.title,
        "body": self.body
      }
    
        