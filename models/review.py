#!/usr/bin/env python3
""" Imported modules """

from models.base_model import BaseModel


class Review(BaseModel):
    """ The class methods and attributes """
    place_id = ""
    user_id = ""
    text = ""
