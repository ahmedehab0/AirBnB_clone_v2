#!/usr/bin/python3
"""engine that user sqlalchemy"""

import models
from os import getenv
from models.base_model import Base
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    """engine class"""

    __engine = None
    __session = None

    def __init__(self):
        """create engine for the database"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(getenv('HBNB_MYSQL_USER'),
                                                                           getenv('HBNB_MYSQL_PWD'),
                                                                           getenv('HBNB_MYSQL_HOST'),
                                                                           getenv('HBNB_MYSQL_DB'), pool_pre_ping=True))

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """
        query for all objects on the current database session
        """        
        classes = {
            "City": City,
            "State": State,
            "User": User,
            "Place": Place,
            "Review": Review,
            "Amenity": Amenity,
        }
        new_dict = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query_rows = self.__session.query(cls)
            for obj in query_rows:
                key = obj.__class__.__name__ + '.' + obj.id
                new_dict[key] = obj
            return new_dict

        else:
            for name, value in classes.items():
                try:
                    query_rows = self.__session.query(value)
                except Exception:
                    continue
                for obj in query_rows:
                    key = name + '.' + obj.id
                    new_dict[key] = obj
            return new_dict
    def new(self, obj):
        """add the objedt to the current database"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()
