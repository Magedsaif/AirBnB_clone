#!/usr/bin/python3
"""state model."""
from models.base_model import BaseModel


class State(BaseModel):
    """state class."""

    def __init__(self, *args, **kwargs):
        """Instance Constructor.

        args
        name : string state email
        """
        if not kwargs:
            self.name = ""
        super().__init__(*args, **kwargs)
