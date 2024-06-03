#!/usr/bin/python3

"""defines the class Review"""

import models


class Review(models.BaseModel):
    """defines Review based on BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
