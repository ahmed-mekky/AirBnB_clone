from models.engine.file_storage import FileStorage

classes = {"BaseModel": BaseModel, "User": User}
storage = FileStorage()
# Call reload() method on the storage variable
storage.reload()
