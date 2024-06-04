#!/usr/bin/python3

"""defines the class BaseModel"""

from datetime import datetime, date, time
import uuid
import models


class BaseModel:
    """base class for user, city, place, etc."""
    def __init__(self, *args, **kwargs):
        """initializes BaseModel with unique id and creation date"""

        if kwargs:

            for key, value in kwargs.items():
                # If created_at or updated_at are in kwargs,
                # they will be overwritten with datetime format
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                # loop through user input for any other key/value pairs
                # initialize anything entered except for __class__
                if key != "__class__":
                    setattr(self, key, value)

        else:
            # normal instantiation if no kwargs
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        """sets updated_at attribute to current time

        also updates json objects list
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """creates dictionary representation of BaseModel

        Returns:
            all BaseModel attributes and class name as dictionary
        """

        attr_dict = {}

        # first adds class name to dictionary
        attr_dict.update({'__class__': self.__class__.__name__})

        # adds all other attributes
        # created_at/updated_at values converted to isoformat here
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                attr_dict.update({key: value.isoformat()})
            else:
                attr_dict.update({key: value})

        return attr_dict

    def __str__(self):
        """re-formats print output for BaseModel

        Returns:
            object formatted as [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
