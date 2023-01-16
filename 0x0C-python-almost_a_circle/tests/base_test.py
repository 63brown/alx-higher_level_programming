#!/usr/bin/python3
"""Unittest cases for Base class"""
import unittest
import inspect
import pep8
import json
from models import base
from models.base import Base


class TestBaseDocs(unittest.TestCase):
    """Tests for Base documentation"""
    @classmethod
    def setUpClass(cls):
        "Makes sure all prerequisites for our tests are available"

        """gives only members from Base members, in a list,
         which have true values for our predicate(2nd arg)"""
        cls.basefuncs = inspect.getmembers(Base, inspect.isfunction)

    @classmethod
    def tearDownClass(cls):
        """Cleans all those prerequisites"""
        cls.basefuncs = []

    def test_base_conforms_pep8(self):
        """Test models/base.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_testbase_conforms_pep8(self):
        """Test that tests/test_models/test_base.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_base.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_module_docstr(self):
        """Tests for base module docstring"""
        self.assertTrue(len(base.__doc__) >= 1)

    def test_class_docstr(self):
        """Tests for Base class docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for base functions docstrings"""
        for func in self.basefuncs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestBase(unittest.TestCase):
    """Tests for Base class"""
    def test_extra_args(self):
        """Tests extra arguments upon initialization"""
        with self.assertRaises(Exception):
            Base(1, 1)

    def test_isid(self):
        """Tests if there is id"""
        c = Base(12)
        other = Base()
        self.assertEqual(c.id, 12)
        self.assertEqual(other.id, 1)

    def test_nb_objects(self):
        """Tests private attribute nb_objects"""
        a = Base(2)
        with self.assertRaises(Exception):
            print(a.nb_objects)
        with self.assertRaises(Exception):
            print(a.__nb_objects)

    def test_to_json_string(self):
        """Tests to_json_string"""
        Base._Base__nb_objects = 0
        a = {"id": 1, "width": 3, "height": 6, "x": 8, "y": 5}
        b = {"id": 2, "width": 6, "height": 12, "x": 10, "y": 6}
        my_str = Base.to_json_string([a, b])
        self.assertTrue(type(my_str) is str)
        c = json.loads(my_str)
        self.assertEqual(c, [a, b])
        self.assertEqual("[]", Base.to_json_string([]))

    def test_from_json_string(self):
        """Tests from_json_string"""
        a = '[{"id": 3, "width": 4, "height": 5, "x": 6, "y": 7}]'
        my_obj = Base.from_json_string(a)
        self.assertTrue(type(my_obj) is list)
        self.assertEqual(len(my_obj), 1)
        self.assertTrue(type(my_obj[0]) is dict)
        self.assertEqual(my_obj[0],
                         {"id": 3, "width": 4, "height": 5, "x": 6, "y": 7})
        self.assertEqual([], Base.from_json_string(""))
