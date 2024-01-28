#!/usr/bin/python3
"""base model of the airbnb"""
import uuid
import datetime
import storage


class BaseModel:
    """base class"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            storage.new()
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.datetime.now()

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        class_dict = dict()
        for key, value in self.__dict__.items():
            class_dict[key] = value
            if key == "created_at" or key == "updated_at":
                class_dict[key] = value.isoformat()
        class_dict["__class__"] = self.__class__.__name__
        return class_dict