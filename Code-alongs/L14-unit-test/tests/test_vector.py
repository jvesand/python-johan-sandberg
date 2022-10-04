from __future__ import annotations
import sys, os
import unittest

print(__file__)

# we change directory to where this file is
os.chdir(os.path.dirname(__file__))

# defins a path that is one folder up
# in this path we have vector.py and plotter.py
path_to_vector_module = os.path.abspath("../")

# python looks in sys.path for modules
sys.path.append(path_to_vector_module)
print(path_to_vector_module)

from vector import Vector

# inherits from unittest.TestCase
class TestVector(unittest.TestCase):
    # always runs... like init???
    # setUp gives attributes that we can use later on
    # this is to avoid repeating too much code
    def setUp(self):
        self.x, self.y = 1, 2

    # used to create default 2D vector for testing
    def create_2D_vector(self) -> Vector:
        return Vector(self.x, self.y)

    def test_create_2D_vector(self):
        """Testing numbers property"""
        # v = Vector(1,2)
        v = self.create_2D_vector()
        self.assertEqual(v.numbers, (1,2))

    def test_create_3D_vector(self):
        v = Vector(1,2,3)
        self.assertEqual(v.numbers, (1,2,3))

    def test_create_empy_vector(self):
        # if we get a raised ValueError the test is OK
        with self.assertRaises(ValueError):
            v = Vector()

    def test_equal_2D_vectors(self):
        v1 = self.create_2D_vector()
        v2 = Vector(1,2)
        self.assertEqual(v1, v2)

    def test_not_equal_2D_vectors(self):
        v1 = self.create_2D_vector()
        v2 = Vector(1,-2)
        self.assertNotEqual(v1, v2)

    def test_add_2_vectors(self):
        v1 = self.create_2D_vector()
        v2 = Vector(1,3)
        self.assertEqual(v1 + v2, Vector(self.x+1, self.y+3))

    def test_getitem(self):
        v1 = self.create_2D_vector()

        # this approach is tedious in many dimensions
        # self.assertEqual(v1[0], self.x)
        # self.assertEqual(v1[1], self.y)

        for i, number in enumerate((1,2)):
            self.assertEqual(v1[i], number)

    # TODO: many more tests to be performed

# if module runs now this is true
# but if imported from somewhere else, it is not
if __name__ == "__main__":
    unittest.main() # runs all tests from unittest classes and subclasses