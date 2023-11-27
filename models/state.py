"""state module"""


import models
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """state class"""

    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable = False)
        cities = relationship("City", backref="state", cascade="delete")

    else:
        @property
        def cities(self):
            "getter for list of city instances related to the state"
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)

            return city_list
