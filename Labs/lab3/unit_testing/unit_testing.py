import sys, os
import unittest

# changes directory to current directory
os.chdir(os.path.dirname(__file__))

# appends parent directory to sys.path
sys.path.append(os.path.abspath("../"))

from geometry_shapes import *


class TestShape(unittest.TestCase):
    def setUp(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def create_shape(self) -> Shape:
        return Shape(self.x, self.y, self.z)

    def test_create_shape1(self):
        with self.assertRaises(TypeError):
            shape1 = Shape()

    def test_create_shape2(self):
        with self.assertRaises(TypeError):
            shape1 = Shape("test", 0, 0)


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.x = 0
        self.y = 0
        self.side1 = 10
        self.side2 = 10

    def create_rectangle(self) -> Rectangle:
        return Rectangle(self.x, self.y, self.side1, self.side2)

    def test_create_rectangle1(self):
        with self.assertRaises(TypeError):
            rect1 = Rectangle(0,0, "test", 10)

    def test_create_rectangle2(self):
        with self.assertRaises(ValueError):
            rect1 = Rectangle(0,0, -1, 10)

    def test_parameters(self):
        rect1 = Rectangle(1,2,3,4)
        self.assertEqual((1,2,3,4), (rect1.x, rect1.y, rect1.side1, rect1.side2))

    def test_is_inside1(self):
        rect1 = self.create_rectangle()
        self.assertTrue(rect1.is_inside(0,0))

    def test_is_inside2(self):
        rect1 = self.create_rectangle()
        self.assertFalse(rect1.is_inside(20,20))

    # def test_translation(self):
        # rect1 = self.create_rectangle()
        # rect1.translate(20,20)
        # rect2 = Rectangle(20, 20, 10, 10)
        # self.assertEqual((rect1.x, rect1.y), (rect2.x, rect2.y))

    def test_equality1(self):
        rect1 = self.create_rectangle()
        rect2 = self.create_rectangle()
        self.assertTrue(rect1 == rect2)

    def test_equality2(self):
        rect1 = self.create_rectangle()
        rect2 = Rectangle(10,10,10,10)
        self.assertFalse(rect1 == rect2)

    def test_operators1(self):
        rect1 = self.create_rectangle()
        rect2 = Rectangle(0,0,100,100)
        self.assertTrue(rect1 < rect2)

    def test_operators2(self):
        rect1 = self.create_rectangle()
        rect2 = Rectangle(1,1,10,10)
        self.assertTrue(rect1 <= rect2)

    def test_operators3(self):
        rect1 = self.create_rectangle()
        rect2 = Rectangle(10,10,50,50)
        self.assertTrue(rect2 > rect1)

    def test_operators4(self):
        rect1 = self.create_rectangle()
        rect2 = Rectangle(10,10,10,10)
        self.assertTrue(rect2 >= rect1)


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.x = 0
        self.y = 0
        self.radius = 10

    def create_circle(self) -> Circle:
        return Circle(self.x, self.y, self.radius)

    def test_create_circle(self):
        with self.assertRaises(TypeError):
            circ1 = Circle(0,0, "test")

    def test_create_circle2(self):
        with self.assertRaises(ValueError):
            circ1 = Circle(0,0, -1)

    def test_parameters(self):
        circ1 = Circle(1,2,3)
        self.assertEqual((1,2,3), (circ1.x, circ1.y, circ1.radius))

    def test_is_inside1(self):
        circ1 = self.create_circle()
        self.assertTrue(circ1.is_inside(0,0))

    def test_is_inside2(self):
        circ1 = self.create_circle()
        self.assertFalse(circ1.is_inside(20,20))

    # def test_translation(self):
    #     circ1 = self.create_circle()
    #     circ1.translate(20,20)
    #     circ2 = Circle(20, 20, 10)
    #     self.assertEqual((circ1.x, circ1.y), (circ2.x, circ2.y))

    def test_equality1(self):
        circ1 = self.create_circle()
        circ2 = self.create_circle()
        self.assertTrue(circ1 == circ2)

    def test_equality2(self):
        circ1 = self.create_circle()
        circ2 = Circle(10,10,10)
        self.assertFalse(circ1 == circ2)

    def test_operators1(self):
        circ1 = self.create_circle()
        circ2 = Circle(0,0,100)
        self.assertTrue(circ1 < circ2)

    def test_operators2(self):
        circ1 = self.create_circle()
        circ2 = Circle(1,1,10)
        self.assertTrue(circ1 <= circ2)

    def test_operators3(self):
        circ1 = self.create_circle()
        circ2 = Circle(10,10,50)
        self.assertTrue(circ2 > circ1)

    def test_operators4(self):
        circ1 = self.create_circle()
        circ2 = Circle(10,10,10)
        self.assertTrue(circ2 >= circ1)        


class TestCube(unittest.TestCase):
    def setUp(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.side1 = 10
        self.side2 = 10
        self.side3 = 10

    def create_cube(self) -> Cube:
        return Cube(self.x, self.y, self.z, self.side1, self.side2, self.side3)

    def test_create_cube1(self):
        with self.assertRaises(TypeError):
            cube1 = Cube(0,0,0, 10, 10, "test")

    def test_create_cube2(self):
        with self.assertRaises(ValueError):
            cube1 = Cube(0,0,0, 10, 10, -1)

    def test_parameters(self):
        cube1 = Cube(1,2,3,4,5,6)
        self.assertEqual((1,2,3,4,5,6), (cube1.x, cube1.y, cube1.z, cube1.side1, cube1.side2, cube1.side3))

    def test_is_inside1(self):
        cube1 = self.create_cube()
        self.assertTrue(cube1.is_inside(0,0,z=0))

    def test_is_inside2(self):
        cube1 = self.create_cube()
        self.assertFalse(cube1.is_inside(20,20,z=20))

    # def test_translation(self):
    #     cube1 = self.create_cube()
    #     cube1.translate(20,20,20)
    #     cube2 = Cube(20, 20, 20, 10, 10, 10)
    #     self.assertEqual((cube1.x, cube1.y, cube1.z), (cube2.x, cube2.y, cube2.z))

    def test_equality1(self):
        cube1 = self.create_cube()
        cube2 = self.create_cube()
        self.assertTrue(cube1 == cube2)

    def test_equality2(self):
        cube1 = self.create_cube()
        cube2 = Cube(10,10,10,10,10,10)
        self.assertFalse(cube1 == cube2)

    def test_operators1(self):
        cube1 = self.create_cube()
        cube2 = Cube(0,0,0,100,100,100)
        self.assertTrue(cube1 < cube2)

    def test_operators2(self):
        cube1 = self.create_cube()
        cube2 = Cube(1,1,1, 10,10,10)
        self.assertTrue(cube1 <= cube2)

    def test_operators3(self):
        cube1 = self.create_cube()
        cube2 = Cube(10,10,10, 50,50,50)
        self.assertTrue(cube2 > cube1)

    def test_operators4(self):
        cube1 = self.create_cube()
        cube2 = Cube(10,10,10, 10,10, 10)
        self.assertTrue(cube2 >= cube1)


class TestSphere(unittest.TestCase):
    def setUp(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.radius = 10

    def create_sphere(self) -> Sphere:
        return Sphere(self.x, self.y, self.z, self.radius)

    def test_create_sphere1(self):
        with self.assertRaises(TypeError):
            sphere1 = Sphere(0,0,0, "test")

    def test_create_sphere2(self):
        with self.assertRaises(ValueError):
            sphere1 = Sphere(0,0,0, -1)

    def test_parameters(self):
        sphere1 = Sphere(1,2,3,4)
        self.assertEqual((1,2,3,4), (sphere1.x, sphere1.y, sphere1.z, sphere1.radius))

    def test_is_inside1(self):
        sphere1 = self.create_sphere()
        self.assertTrue(sphere1.is_inside(0,0,z=0))

    def test_is_inside2(self):
        sphere1 = self.create_sphere()
        self.assertFalse(sphere1.is_inside(20,20,z=20))

    # def test_translation(self):
    #     sphere1 = self.create_sphere()
    #     sphere1.translate(20,20,20)
    #     sphere2 = Sphere(20, 20, 20, 10)
    #     self.assertEqual((sphere1.x, sphere1.y, sphere1.z), (sphere2.x, sphere2.y, sphere2.z))

    def test_equality1(self):
        sphere1 = self.create_sphere()
        sphere2 = self.create_sphere()
        self.assertTrue(sphere1 == sphere2)

    def test_equality2(self):
        sphere1 = self.create_sphere()
        sphere2 = Sphere(10,10,10,10)
        self.assertFalse(sphere1 == sphere2)

    def test_operators1(self):
        sphere1 = self.create_sphere()
        sphere2 = Sphere(0,0,0,100)
        self.assertTrue(sphere1 < sphere2)

    def test_operators2(self):
        sphere1 = self.create_sphere()
        sphere2 = Sphere(1,1,1, 10)
        self.assertTrue(sphere1 <= sphere2)

    def test_operators3(self):
        sphere1 = self.create_sphere()
        sphere2 = Sphere(10,10,10, 50)
        self.assertTrue(sphere2 > sphere1)

    def test_operators4(self):
        sphere1 = self.create_sphere()
        sphere2 = Sphere(10,10,10, 10)
        self.assertTrue(sphere2 >= sphere1)        

if __name__ == "__main__":
    unittest.main() # runs all tests        