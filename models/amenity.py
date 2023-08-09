#!/usr/bin/python3
"""amenity model."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """amenity class."""

    def __init__(self, *args, **kwargs):
        """Instance Constructor.

        args
        name : string amenity name
        """
        super().__init__()
        self.name = ""
