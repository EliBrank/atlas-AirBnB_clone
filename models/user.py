#!/usr/bin/python3

"""defines the class User"""

import models


class User(models.BaseModel):
    """defines User based on BaseModel"""
    def __init__(self, email=None, password=None, first_name=None,
                last_name=None, *args, **kwargs):
        """initializes User

        Args:
            email: email address for User (string)
            password: password for User (string)
            first_name: User's first name (string)
            last_name: User's last name (string)
        """

        super().__init__()

        if email is not None:
            self.email = email

        if password is not None:
            self.password = password

        if first_name is not None:
            self.first_name = first_name

        if last_name is not None:
            self.last_name = last_name
