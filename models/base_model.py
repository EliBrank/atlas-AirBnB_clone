#!/usr/bin/python3

"""defines the class BaseModel"""

from datetime import *
import uuid


class BaseModel:
    def __init__(self, id="", created_at=0, updated_at=0):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        # self.created_at = datetime.strptime(f"{self.created_at}", "%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.created_at



    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id})({self.__dict__})"

# %Y-%m-%dT%H:%M:%S.%f
id = BaseModel(1)
id2 = BaseModel()
print(id.created_at)
print(id2.created_at)
print(id)