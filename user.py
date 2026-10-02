from baseEntity import BaseEntity

class User(BaseEntity):
  def __init__(self, id, name, email):
      super().__init__(id)
      self.__name = name
      self.__email= email
      
  @property
  def name(self):
    return self.__name
  
  @property
  def email(self):
    return self.__email
  
  def to_dict(self):
    return {
      "type": "User",
      "id": self.id,
      "name": self.name,
      "email": self.email
    }
  
  