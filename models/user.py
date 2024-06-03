#!/usr/bin/python3

"""defines the class User"""

import models


class User(models.BaseModel):
    """defines User based on BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
