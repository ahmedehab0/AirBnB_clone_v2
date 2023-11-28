"""amenity module"""


import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity class"""

    __tablename__ = "amenities"

    name = Column(String(128), nullable = False)
    place_amenitites = relationship("Place", secondary="place_amenity", viewonly=False)
