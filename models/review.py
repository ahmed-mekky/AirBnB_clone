from models.base_model import BaseModel


class Review(BaseModel):
    """Main Review Class"""

    place_id = ""
    user_id = ""
    text = ""
