"""
Review (models/review.py):
Public class attributes:
place_id: string - empty string: it will be the Place.id
user_id: string - empty string: it will be the User.id
text: string - empty string
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class code here """
    place_id = ""
    user_id = ""
    text = ""
