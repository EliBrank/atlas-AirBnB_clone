#!/usr/bin/python3

"""defines the class BaseModel"""

import datetime, uuid


class BaseModel:
    __id = 0
    def __init__(self, id=uuid.uuid4()):
        if id is None:
            BaseModel.__id += 1
            self.id = BaseModel.__id
        else:
            self.id = id

    # def __str__(self):
    #     return f"[{cls.__name__}] ({self.id})({self.__dict__})"

id = BaseModel()
print(id.id)