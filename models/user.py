#!/usr/bin/python3
"""
User Model
-----------
Attributes:
    email (str): The email address associated with the user.
    password (str): The user's password.
    first_name (str): The first name of the user.
    last_name (str): The last name of the user.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user in the system.

    Attributes:
        email (str): The email address associated with the user.
        password (str): The user's password.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.

    Args:
        *args: Variable length positional arguments
        **kwargs: Variable keyword arguments
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new User instance.

        Args:
            *args: Variable length positional arguments
            **kwargs: Variable keyword arguments
        """
        super().__init__(*args, **kwargs)
