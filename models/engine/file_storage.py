import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON files"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as json_file:
            json.dump(serialized_objects, json_file)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }

        file_content = {}
        try:
            with open(self.__file_path, "r") as json_file:
                file_content = json.load(json_file)
                for key, obj in file_content.items():
                    self.all()[key] = classes[obj.get("__class__")](**obj)
        except FileNotFoundError:
            pass
