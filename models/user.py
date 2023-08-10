#!/usr/bin/python3
"""user model."""
from models.base_model import BaseModel


class User(BaseModel):
    """user class."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Instance Constructor.

        args
        email : string user email
        password: string user password
        first_name: string user first_name
        last_name: string user last_name
        """
        super().__init__(*args, **kwargs)
