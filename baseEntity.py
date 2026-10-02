from abc import ABC, abstractmethod

class BaseEntity(ABC):
    def __init__(self, id):
         if not isinstance(id, int):
            raise TypeError("id phải là số nguyên.")

         if id <= 0:
            raise ValueError("id phải lớn hơn 0.")
         self.__id = id
        
    @property
    def id(self):
      return self.__id
    
    @abstractmethod
    def to_dict(self):
      pass

        
    
  