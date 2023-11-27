"""amenity module"""


import models
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity class"""

    __tablename__ = "amenities"

    name = Column(String(128), nullable = False)
    place_amenities = relationship("Place", secondary="place_amenity", viewonly=False)
