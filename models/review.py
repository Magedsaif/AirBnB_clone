#!/usr/bin/python3
"""review model."""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class."""

    def __init__(self, *args, **kwargs):
        """Instance Constructor.

        args
        name : string review email
        """
        super().__init__()
        self.place_id = ""  # Place.id
        self.user_id = ""  # User.id
        self.text = ""
