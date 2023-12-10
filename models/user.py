#!/usr/bin/env python3
""" Imported modules """

from models.base_model import BaseModel


class User(BaseModel):
    """ The class methods and attributes """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
