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
        super().__init__()
        self.state_id = ""  # State.id
        self.name = ""
