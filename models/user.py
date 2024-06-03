#!/usr/bin/python3

"""defines the class User"""

import models


class User(models.BaseModel):
    """defines User based on BaseModel"""
    def __init__(self, email="", password="", first_name="", last_name="",
                *args, **kwargs):
        """initializes User

        Args:
            email: email address for User (string)
            password: password for User (string)
            first_name: User's first name (string)
            last_name: User's last name (string)
        """

        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self. last_name = last_name

# Public class attributes:
#
#     email: string - empty string
#     password: string - empty string
#     first_name: string - empty string
#     last_name: string - empty string
