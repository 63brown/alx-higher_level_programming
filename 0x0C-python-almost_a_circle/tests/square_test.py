#!/usr/bin/python3
"""Unittest cases for Square class"""
import unittest
import inspect
import pep8
import json
from models.base import Base
from models import square
from models.square import Square


class TestSquareDocs(unittest.TestCase):
    """Tests for Square documentation"""
    @classmethod
    def setUpClass(cls):
        "Makes sure all prerequisites for our tests are available"

        """gives only members from Square members, in a list,
         which have true values for our predicate(2nd arg)"""
        cls.sqrfuncs = inspect.getmembers(Square, inspect.isfunction)

    @classmethod
    def tearDownClass(cls):
        """Cleans all those prerequisites"""
        cls.sqrfuncs = []

    def test_Square_conforms_pep8(self):
        """Test models/square.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/square.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_testSquare_conforms_pep8(self):
        """Test that tests/test_models/test_square.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_square.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_module_docstr(self):
        """Tests for the module docstring"""
        self.assertTrue(len(square.__doc__) >= 1)

    def test_class_docstr(self):
        """Tests for Square class docstring"""
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for square functions docstrings"""
        for func in self.sqrfuncs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestSquare(unittest.TestCase):
    """Tests for Square class"""
    @classmethod
    def setUpClass(cls):
        """Makes sure all prerequisites for our tests are available"""
        Base._Base__nb_objects = 0
        cls.a = Square(9)
        cls.b = Square(5, 6)
        cls.c = Square(8, 4, 10)
        cls.d = Square(6, 9, 7, 11)

    def test_isid(self):
        """Tests if there is id"""
        self.assertEqual(self.a.id, 1)
        self.assertEqual(self.d.id, 11)

    def test_size(self):
        """Tests size"""
        self.assertEqual(self.a.size, 9)
        self.assertEqual(self.c.size, 8)

    def test_width(self):
        """Tests width"""
        self.assertEqual(self.a.width, 9)
        self.assertEqual(self.c.width, 8)

    def test_height(self):
        """Tests height"""
        self.assertEqual(self.a.height, 9)
        self.assertEqual(self.b.height, 5)

    def test_x(self):
        """Tests x"""
        self.assertEqual(self.a.x, 0)
        self.assertEqual(self.d.x, 9)

    def test_y(self):
        """Tests y"""
        self.assertEqual(self.b.y, 0)
        self.assertEqual(self.d.y, 7)

    def test_empty(self):
        """Tests when given no values"""
        with self.assertRaises(TypeError):
            Square()

    def test_non_int(self):
        """Tests non-integers for any values"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_zero_orless(self):
        """Tests if less than zero or zero for width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_less_zero(self):
        """Tests if less than zero for x, y values"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def test_area(self):
        """Tests area"""
        self.assertEqual(self.a.area(), 81)
        self.assertEqual(self.d.area(), 36)

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
        a = Square(2, 3, 4, 5)
        self.assertEqual("[Square] (5) 3/4 - 2", str(a))

    def test_update_args(self):
        """Tests the udpate method with args"""
        n = Square(1, 0, 0, 1)
        self.assertEqual(str(n), "[Square] (1) 0/0 - 1")
        n.update()
        self.assertEqual(str(n), "[Square] (1) 0/0 - 1")
        n.update(10)
        self.assertEqual(str(n), "[Square] (10) 0/0 - 1")
        n.update(11, 4, 2)
        self.assertEqual(str(n), "[Square] (11) 2/0 - 4")
        n.update(11, 4, 2, 6)
        self.assertEqual(str(n), "[Square] (11) 2/6 - 4")
        n.update(11, 4, 2, 6, 7)
        self.assertEqual(str(n), "[Square] (11) 2/6 - 4")

    def test_update_kwargs(self):
        """Tests the update method with kwargs"""
        m = Square(1, 0, 0, 1)
        self.assertEqual(str(m), "[Square] (1) 0/0 - 1")
        m.update()
        self.assertEqual(str(m), "[Square] (1) 0/0 - 1")
        m.update(size=6)
        self.assertEqual(str(m), "[Square] (1) 0/0 - 6")
        m.update(size=5, x=3)
        self.assertEqual(str(m), "[Square] (1) 3/0 - 5")
        m.update(x=5, y=4, id=12)
        self.assertEqual(str(m), "[Square] (12) 5/4 - 5")
        m.update(extra=11)
        self.assertEqual(str(m), "[Square] (12) 5/4 - 5")

    def test_update_args_kwargs(self):
        """Tests the update method with both args and kwargs"""
        p = Square(1, 0, 0, 1)
        p.update(11, 4, 2, 6, width=5, height=6, x=7, y=8, id=9)
        self.assertEqual(str(p), "[Square] (11) 2/6 - 4")

    def test_save_to_file(self):
        """Tests save_to_file"""
        a = Square(1, 2, 3, 4)
        b = Square(5, 4, 3, 2)
        c = [a, b]
        d = []
        Square.save_to_file(c)
        with open("Square.json", "r") as f:
            my_obj = [a.to_dictionary(), b.to_dictionary()]
            self.assertEqual(json.dumps(my_obj), f.read())
        Square.save_to_file(d)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_create(self):
        """Tests create"""
        a = {"id": 3, "size": 3, "x": 5, "y": 2}
        b = {"id": 4, "size": 4, "x": 6, "y": 7}
        m = Square.create(**a)
        n = Square.create(**b)
        self.assertEqual("[Square] (3) 5/2 - 3", str(m))
        self.assertEqual("[Square] (4) 6/7 - 4", str(n))
        self.assertIsNot(a, m)
        self.assertIsNot(b, n)
        self.assertNotEqual(a, m)
        self.assertNotEqual(b, n)

    def test_load_from_file(self):
        """Tests load_from_file"""
        a = Square(1, 2, 3, 4)
        b = Square(5, 4, 3, 2)
        c = [a, b]
        Square.save_to_file(c)
        d = Square.load_from_file()
        self.assertTrue(type(d) is list)
        self.assertEqual(len(d), 2)
        e = d[0]
        f = d[1]
        self.assertTrue(type(e) is Square)
        self.assertTrue(type(f) is Square)
        self.assertEqual(str(a), str(e))
        self.assertEqual(str(b), str(f))
        self.assertIsNot(a, e)
        self.assertIsNot(b, f)
        self.assertNotEqual(a, e)
        self.assertNotEqual(b, f)
