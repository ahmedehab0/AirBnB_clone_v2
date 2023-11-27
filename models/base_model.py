"""base module"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, DateTime
import datetime
import uuid
import models

Base = declarative_base()

class BaseModel:
    """base model that defines all common attributes
    for other classes"""

    id = Column(String(60), nullable = False, primary_key = True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow(), nullable = False)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow(), nullable = False)
    def __init__(self, *args, **kwargs):
        """
        initialization method
            id(string): uniqe id for each base model
            created_at: datetime-assign with the current datetime when an
                        instance is created
            updated_at: datetime-assign with the current datetime when an
                        instance is updated
        """
        if kwargs:
            date_form = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    self.__dict__[key] = datetime.datetime.strptime(value,
                                                                    date_form)
                elif key == "__class__":
                    pass
                else:
                    self.__dict__[key] = value

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """return represantation of the class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of
        the instance"""
        hash_table = {}
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                hash_table[key] = value.isoformat()
            else:
                hash_table[key] = value
        hash_table["__class__"] = self.__class__.__name__
        if '_sa_instance_state' in hash_table:
            del hash_table['_sa_instance_state']
        return hash_table

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
