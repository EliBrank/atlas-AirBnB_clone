#!/usr/bin/python3

"""defines the class BaseModel"""

from datetime import datetime, date, time
import uuid


class BaseModel:
    """base class for city, place, etc."""
    def __init__(self):
        """initializes BaseModel with unique id and creation date"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        # self.created_at = datetime.strptime(f"{self.created_at}", "%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.created_at

    def save(self):
        """sets updated_at attribute to current time"""
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        attr_dict = {attr: getattr(self, attr) for attr in self.__dict__}
        attr_dict.update({'__class__' : self.__class__.__name__})
        return attr_dict

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id})({self.__dict__})"

# %Y-%m-%dT%H:%M:%S.%f
# id = BaseModel()
# id2 = BaseModel()
# print(id.created_at)
# print(id.updated_at)
# id.save()

# print(id.updated_at)
