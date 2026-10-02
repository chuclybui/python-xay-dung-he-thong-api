from abc import ABC, abstractmethod

class BaseEntity(ABC):
    def __init__(self, id):
        self.__id = id
        
    @property
    def id(self):
      return self.__id
    
    @abstractmethod
    def to_dict(self):
      pass

        
    
  