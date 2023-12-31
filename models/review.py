"""review module"""


import models
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, Column, String, ForeignKey


class Review(BaseModel, Base):
    """review class"""

    __tablename__ = "reviews"

    text = Column(String(1024), nullable = False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable = False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
