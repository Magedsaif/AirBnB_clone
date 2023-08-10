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

        if not kwargs:
            self.place_id = ""  # Place.id
            self.user_id = ""  # User.id
            self.text = ""
        super().__init__(*args, **kwargs)
