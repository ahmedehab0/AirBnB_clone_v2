"""city module"""


import models
from models.base_model import BaseModel, Base
from sqlalchemy import String, ForeignKey, Column
from models.state import State

class City(BaseModel, Base):
    """city class"""

    __tablename__ = "cities"
    name = Column(String(128), nullable = False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable = False)
