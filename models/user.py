"""user class module"""


import models
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship



class User(BaseModel, Base):
    """user class"""

    __tablename__ = "users"

    email = Column(String(128), nullable = False)
    password = Column(String(128), nullable = False)
    first_name = Column(String(128), nullable = True)
    last_name = Column(String(128), nullable = True)
    places = relationship("Place", backref="user")
    reviews = relationship("Review", backref="user")
