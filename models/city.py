#!/usr/bin/python3
"""city model."""
from models.base_model import BaseModel


class City(BaseModel):
    """city class."""

    def __init__(self, *args, **kwargs):
        """Instance Constructor.

        args
        name : string city name
        state_id : string State.id
        """
        if not kwargs:
            self.state_id = ""  # State.id
            self.name = ""
        super().__init__(*args, **kwargs)
        
