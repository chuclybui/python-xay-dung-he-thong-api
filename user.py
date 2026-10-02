from baseEntity import BaseEntity

class User(BaseEntity):
  def __init__(self, id, name, email):
      super().__init__(id)
      if not isinstance(name, str):
            raise TypeError("name phải là chuỗi.")

      if not name.strip():
            raise ValueError("name không được để trống.")

      if not isinstance(email, str):
            raise TypeError("email phải là chuỗi.")

      if not email.strip():
            raise ValueError("email không được để trống.")

      if "@" not in email:
            raise ValueError("email không hợp lệ.")

      self.__name = name.strip()
      self.__email = email.strip()
      
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
  
  