"""place module"""


import models
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from sqlalchemy import Integer, Column, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """place class"""

    __tablename__ = "places"
    
    amenity_ids = []
    
    if getenv('HBNB_TYPE_STORAGE') == "db":
        city_id = Column(String(60), ForeignKey('cities.id'), nullable = False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable = False)
        name = Column(String(128), nullable = False)
        description = Column(String(1024), nullable = True)
        number_rooms = Column(Integer, nullable = False, default=0)
        number_bathrooms = Column(Integer, nullable = False, default=0)
        max_guest = Column(Integer, nullable = False, default=0)
        price_by_night = Column(Integer, nullable = False, default=0)
        latitude = Column(Float, nullable = True)
        longitude = Column(Float, nullable = True)
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity", viewonly = False)
    else:
        @property
        def reviews(self):
            reviews_list = []
            all_reviews = models.storage.all(Review)

            for review in all_reviews.values():
                if review.place_id == self.id:
                    reviews_list.append(review)

            return reviews_list

        @property
        def amenities(self):
            amenities_list = []
            all_amenities = models.storage.all(Amenity)

            for value in all_amenities.values():
                if value.id == self.amenity_ids:
                    amenities_list.append(value)
            return amenities_list
