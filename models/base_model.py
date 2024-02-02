import uuid
import datetime


class BaseModel:
    """Base class for other classes"""

    def __init__(self, *args, **kwargs):
        from models import storage

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"
                        )
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        from models import storage

        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        class_dict = dict(self.__dict__)
        class_dict["created_at"] = self.created_at.isoformat()
        class_dict["updated_at"] = self.updated_at.isoformat()
        class_dict["__class__"] = self.__class__.__name__
        return class_dict
