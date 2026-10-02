from baseEntity import BaseEntity

class Post(BaseEntity):
    def __init__(self, id, title, body):
      super().__init__(id)
      self.__title = title
      self.__body = body
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
    
        