#!/usr/bin/python3

import unittest
import sys
import models
from time import sleep
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """unittest class for BaseModel class"""

    def test_id(self):
        """test for a uniqe id"""
        self.model1 = BaseModel()
        self.model2 = BaseModel()
        self.assertNotEqual(self.model1.id, self.model2.id)

    def test_str_method(self):
        """test for the __str__ method"""
        dt = datetime.today()
        model1 = BaseModel()
        dt_repr = repr(dt)
        model1.id = "123456"
        model1.created_at = model1.updated_at = dt
        bmstr = model1.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_two_models_different_created_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_save(self):
        """test the save method"""
        model1 = BaseModel()
        sleep(0.05)
        model1.save()
        self.assertLess(model1.created_at, model1.updated_at)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())
