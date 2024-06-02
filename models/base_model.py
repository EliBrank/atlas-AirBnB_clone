#!/usr/bin/python3

"""defines the class BaseModel"""

from datetime import datetime, date, time
import uuid

class BaseModel:
    """base class for city, place, etc."""
    def __init__(self, *args, **kwargs):
        """initializes BaseModel with unique id and creation date"""
        from models import storage
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()

        else:
            # normal instantiation if no kwargs
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def to_dict(self):
        """creates dictionary representation of BaseModel

        Returns:
            all BaseModel attributes and class name as dictionary
        """
        attr_dict = {}

        # first adds class name to dictionary
        attr_dict.update({'__class__' : self.__class__.__name__})

        # adds all other attributes
        # created_at/updated_at values converted to isoformat here
        for attr, attr_value in self.__dict__.items():
            if attr == "created_at" or attr == "updated_at":
                attr_dict.update({attr : attr_value.isoformat()})
            else:
                attr_dict.update({attr : attr_value})
        # attr_dict = {attr: getattr(self, attr) for attr in self.__dict__}
        return attr_dict

    def __str__(self):
        """re-formats print output for BaseModel

        Returns:
            object formatted as [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Saves sum"""
        self.updated_at = datetime.now()