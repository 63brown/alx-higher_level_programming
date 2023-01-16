#!/usr/bin/python3
"""Unittest cases for Rectangle class"""
import unittest
import inspect
import pep8
import json
from models.base import Base
from models import rectangle
from models.rectangle import Rectangle


class TestRectangleDocs(unittest.TestCase):
    """Tests for Rectangle documentation"""
    @classmethod
    def setUpClass(cls):
        "Makes sure all prerequisites for our tests are available"

        """gives only members from Rectangle members, in a list,
         which have true values for our predicate(2nd arg)"""
        cls.rectfuncs = inspect.getmembers(Rectangle, inspect.isfunction)

    @classmethod
    def tearDownClass(cls):
        """Cleans all those prerequisites"""
        cls.rectfuncs = []

    def test_rectangle_conforms_pep8(self):
        """Test models/rectangle.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/rectangle.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_testrectangle_conforms_pep8(self):
        """Test that tests/test_models/test_rectangle.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_rectangle.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_module_docstr(self):
        """Tests for the module docstring"""
        self.assertTrue(len(rectangle.__doc__) >= 1)

    def test_class_docstr(self):
        """Tests for Rectangle class docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for rectangle functions docstrings"""
        for func in self.rectfuncs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class"""
    @classmethod
    def setUpClass(cls):
        """Makes sure all prerequisites for our tests are available"""
        Base._Base__nb_objects = 0
        cls.a = Rectangle(9, 8)
        cls.b = Rectangle(5, 6, 7)
        cls.c = Rectangle(8, 4, 10, 11)
        cls.d = Rectangle(6, 9, 7, 11, 12)

    def test_isid(self):
        """Tests if there is id"""
        self.assertEqual(self.a.id, 1)
        self.assertEqual(self.d.id, 12)

    def test_width(self):
        """Tests width"""
        self.assertEqual(self.a.width, 9)
        self.assertEqual(self.c.width, 8)

    def test_height(self):
        """Tests height"""
        self.assertEqual(self.a.height, 8)
        self.assertEqual(self.b.height, 6)

    def test_x(self):
        """Tests x"""
        self.assertEqual(self.a.x, 0)
        self.assertEqual(self.d.x, 7)

    def test_y(self):
        """Tests y"""
        self.assertEqual(self.b.y, 0)
        self.assertEqual(self.d.y, 11)

    def test_empty(self):
        """Tests when given no values"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_non_int(self):
        """Tests non-integers for any values"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_zero_orless(self):
        """Tests if less than zero or zero for width, height values"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def test_less_zero(self):
        """Tests if less than zero for x, y values"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """Tests area"""
        self.assertEqual(self.a.area(), 72)
        self.assertEqual(self.d.area(), 54)

    def test_area_extrargs(self):
        """
        Tests extra arguments in area
        """
        with self.assertRaises(Exception):
            self.b.area(0)

    def test_str(self):
        """
        Tests __str__ method
        """
        a = Rectangle(2, 3, 4, 5, 7)
        self.assertEqual("[Rectangle] (7) 4/5 - 2/3", str(a))

    def test_update_args(self):
        """Tests the udpate method with args"""
        n = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(n), "[Rectangle] (1) 0/0 - 1/1")
        n.update()
        self.assertEqual(str(n), "[Rectangle] (1) 0/0 - 1/1")
        n.update(10)
        self.assertEqual(str(n), "[Rectangle] (10) 0/0 - 1/1")
        n.update(11, 4, 2, 6, 5)
        self.assertEqual(str(n), "[Rectangle] (11) 6/5 - 4/2")
        n.update(11, 4, 2, 6, 5, 7)
        self.assertEqual(str(n), "[Rectangle] (11) 6/5 - 4/2")

    def test_update_kwargs(self):
        """Tests the update method with kwargs"""
        m = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(m), "[Rectangle] (1) 0/0 - 1/1")
        m.update()
        self.assertEqual(str(m), "[Rectangle] (1) 0/0 - 1/1")
        m.update(height=6)
        self.assertEqual(str(m), "[Rectangle] (1) 0/0 - 1/6")
        m.update(width=5, x=7)
        self.assertEqual(str(m), "[Rectangle] (1) 7/0 - 5/6")
        m.update(x=9, y=7, id=12)
        self.assertEqual(str(m), "[Rectangle] (12) 9/7 - 5/6")
        m.update(extra=11)
        self.assertEqual(str(m), "[Rectangle] (12) 9/7 - 5/6")

    def test_update_args_kwargs(self):
        """Tests the update method with both args and kwargs"""
        p = Rectangle(1, 1, 0, 0, 1)
        p.update(11, 4, 2, 6, 5, width=5, height=6, x=7, y=8, id=9)
        self.assertEqual(str(p), "[Rectangle] (11) 6/5 - 4/2")

    def test_save_to_file(self):
        """Tests save_to_file"""
        a = Rectangle(1, 2, 3, 4, 5)
        b = Rectangle(5, 4, 3, 2, 1)
        c = [a, b]
        d = []
        Rectangle.save_to_file(c)
        with open("Rectangle.json", "r") as f:
            my_obj = [a.to_dictionary(), b.to_dictionary()]
            self.assertEqual(json.dumps(my_obj), f.read())
        Rectangle.save_to_file(d)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_create(self):
        """Tests create"""
        a = {"id": 3, "width": 3, "height": 4, "x": 5, "y": 2}
        b = {"id": 4, "width": 4, "height": 5, "x": 6, "y": 7}
        m = Rectangle.create(**a)
        n = Rectangle.create(**b)
        self.assertEqual("[Rectangle] (3) 5/2 - 3/4", str(m))
        self.assertEqual("[Rectangle] (4) 6/7 - 4/5", str(n))
        self.assertIsNot(a, m)
        self.assertIsNot(b, n)
        self.assertNotEqual(a, m)
        self.assertNotEqual(b, n)

    def test_load_from_file(self):
        """Tests load_from_file"""
        a = Rectangle(1, 2, 3, 4, 5)
        b = Rectangle(5, 4, 3, 2, 1)
        c = [a, b]
        Rectangle.save_to_file(c)
        d = Rectangle.load_from_file()
        self.assertTrue(type(d) is list)
        self.assertEqual(len(d), 2)
        e = d[0]
        f = d[1]
        self.assertTrue(type(e) is Rectangle)
        self.assertTrue(type(f) is Rectangle)
        self.assertEqual(str(a), str(e))
        self.assertEqual(str(b), str(f))
        self.assertIsNot(a, e)
        self.assertIsNot(b, f)
        self.assertNotEqual(a, e)
        self.assertNotEqual(b, f)
