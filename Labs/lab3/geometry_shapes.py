from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


class Shape:
    """Parent class to child classes of various geometric shapes"""
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f"x must be either int or float, not {type(value).__name__}")
        self._x = value

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f"y must be either int or float, not {type(value).__name__}")
        self._y = value

    # cross operator overloads based on area (<, >, <=, >=)
    def __lt__(self, other: Shape) -> bool:
        """<, evaluates TRUE if first shape has a smaller area than the second shape"""
        return self.area < other.area

    def __gt__(self, other: Shape) -> bool:
        """>, evaluates TRUE if first shape has a larger area than the second shape"""
        return self.area > other.area

    def __le__(self, other: Shape) -> bool:
        """<=, evaluates TRUE if first shape has an area smaller than or equal to the second shape"""
        return self.area <= other.area

    def __ge__(self, other: Shape) -> bool:
        """>=, evaluates TRUE if first shape has an area larger than or equal to the second shape"""
        return self.area >= other.area

    def translate(self, x: float, y: float, z = 0):
        """Translates shape to given center coordinates. Original shape is plotted in blue; translated shape is plotted in green.
        Note that even if translated shape has more than 2 dimensions, only axes x and y are plotted"""
        fig, ax = plt.subplots()
        self.plot_shape(fig=fig, ax=ax)
        self.x, self.y, self.z = x, y, z
        self.plot_shape(fig=fig, ax=ax, color='green')
        plt.show()

    def __str__(self) -> str:
        return_string = f"An instance of the {self.__class__.__name__} class: {self.__repr__()}\n" \
            f"The {self.__class__.__name__.lower()} has an area of {self.area} and a circumference of {self.circumference}.\n" \
            f"{self.is_unit()}"
        if not self.z == 0:
            return_string += f" Its volume is {self.volume}."
        return return_string


class Rectangle(Shape):
    """Rectangle class, child class of Shape, representing a rectangular geometric shape
    Its methods have been expanded to accomodate three dimensions (Cube child class)
    For rectangles: z = 0 and side 3 = 0"""
    def __init__(self, x: float, y: float, side1: float, side2: float, z = 0, side3 = 0) -> None:
        super().__init__(x, y)
        self.z = z
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @property
    def side1(self) -> float:
        return self._side1

    @side1.setter
    def side1(self, value) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError(f"side1 must be either int or float, not {type(value).__name__}")
        elif value <= 0:
            raise ValueError("side1 must be positive")
        self._side1 = value

    @property
    def side2(self) -> float:
        return self._side2

    @side2.setter
    def side2(self, value) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError(f"side2 must be either int or float, not {type(value).__name__}")
        elif value <= 0:
            raise ValueError("side2 must be positive")
        self._side2 = value

    @property
    def area(self) -> float:
        """Area of the rectangle"""
        return self.side1 * self.side2

    @property
    def circumference(self) -> float:
        """Circumference of rectangle"""
        return_value = (self.side1 + self.side2) * 2
        if not self.side3 == 0:
            return_value = str(return_value) + " (Note: Circumference of rectangle in (x,y) space (side3 set to 0))"
        return return_value

    def is_unit(self) -> str:
        """Checks whether shape has equal sides"""
        the_type = self.__class__.__name__.lower()
        if self.side1 == self.side2 == self.side3:
            return f"The {the_type} has equal sides"
        else:
            return f"The {the_type} has equal sides."

    def is_inside(self, x: float, y: float, z=0) -> bool:
        """Checks whether given coordinates are inside the shape"""
        return (self.x - self.side1/2 <= x <= self.x + self.side1/2) and \
            (self.y - self.side2/2 <= y <= self.y + self.side2/2) and \
                (self.z - self.side3/2 <= z <= self.z + self.side3/2)

    # plotting a rectangle with matplotlib.patches.Rectangle()
    # source: https://www.statology.org/matplotlib-rectangle/
    def plot_shape(self, fig = None, ax = None, color="blue"):
        """Plots rectangle. Note: Only axes x and y are plotted."""        
        # if plotting outside of translation, need to instantiate fig,ax
        if fig == None:
            fig, ax = plt.subplots()
        anchor_x = self.x - self.side1/2
        anchor_y = self.y - self.side2/2
        ax.set_aspect(1)
        ax.add_patch(mpatches.Rectangle((anchor_x, anchor_y), self.side1, self.side2, facecolor=color))
        ax.autoscale(enable=True)
        if fig == None:
            plt.show()

    def __eq__(self, other: Rectangle) -> bool:
        """==, evaluates TRUE if shapes have the same location and shape"""
        if not self.__class__ == other.__class__:
            raise TypeError(f"Can only check equality if both are {self.__class__.__name__.lower()}")
        return (self.x == other.x and self.y == other.y and self.side1 == other.side1 and self.side2 == other.side2 and \
            self.z == other.z and self.side3 == other.side3)

    def __repr__(self) -> str:
        return f"Rectangle(x = {self.x}, y = {self.y}, side1 = {self.side1}, side2 = {self.side2})"


class Circle(Shape):
    """Circle class, child class of Shape, representing a circular geometric shape
    Its methods have been expanded to accomodate three dimensions (Sphere child class)
    For circles: z = 0"""    
    def __init__(self, x: float, y: float, radius: float, z = 0) -> None:
        super().__init__(x, y)
        self.z = z
        self.radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError(f"radius must be either int or float, not {type(value).__name__}")
        elif value <= 0:
            raise ValueError("radius must be positive")        
        self._radius = value

    @property
    def area(self) -> float:
        """Area of circle"""
        return np.pi * self.radius**2

    @property
    def circumference(self) -> float:
        """Circumference of shape"""
        return 2 * np.pi * self.radius

    def is_unit(self) -> str:
        """Checks whether shape has radius 1 and is centered at the origin"""
        the_type = self.__class__.__name__.lower()
        if self.radius == 1 and self.x == 0 and self.y == 0 and self.z == 0:
            return f"The {the_type} is a unit {the_type}."
        else:
            return f"The {the_type} is not a unit {the_type}."

    def is_inside(self, x: float, y: float, z=0) -> bool:
        """Checks whether given coordinates are inside the shape."""
        return np.linalg.norm(np.asarray([x,y,z]) - np.asarray([self.x, self.y, self.z])) <= self.radius

    # plotting a circle using matplotlib.patches.Circle()
    # source: https://www.pythonpool.com/matplotlib-circle/
    def plot_shape(self, fig = None, ax = None, color='blue'):
        """Plots circle. Note: Only axes x and y are plotted."""
        # if plotting outside of translation, need to instantiate fig,ax
        if fig == None:
            fig, ax = plt.subplots()
        ax.set_aspect(1)
        ax.add_patch(mpatches.Circle((self.x, self.y), self.radius, facecolor=color))
        ax.autoscale(enable=True)
        if fig == None:
            plt.show()    

    def __eq__(self, other: Circle) -> bool:
        f"""==, evaluates TRUE if shapes have the same location and radius"""
        if not self.__class__ == other.__class__:
            raise TypeError(f"Can only check equality if both are {self.__class__.__name__.lower()}s")        
        return (self.x == other.x and self.y == other.y and self.z == other.z and self.radius == other.radius)

    def __repr__(self) -> str:
        return f"Circle(x = {self.x}, y = {self.y}, radius = {self.radius})"


class Cube(Rectangle):
    """Cube class, child class of Rectangle, representing a cuboid geometric shape"""
    def __init__(self, x: float, y: float, z: float, side1: float, side2: float, side3: float) -> None:
        super().__init__(x, y, side1, side2)
        self.z = z
        self.side3 = side3

    @property
    def z(self) -> float:
        return self._z

    @z.setter
    def z(self, value) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f"z must be either int or float, not {type(value).__name__}")
        self._z = value        

    @property
    def side3(self) -> float:
        return self._side3

    @side3.setter
    def side3(self, value) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError(f"side3 must be either int or float, not {type(value).__name__}")
        elif value < 0:
            raise ValueError("side3 must be positive")
        self._side3 = value
        
    @property
    def area(self) -> float:
        """Area of cube"""
        return 2 * (self.side1*self.side2 + self.side1*self.side3 + self.side2*self.side3)
    
    @property
    def volume(self) -> float:
        """Volume of cube"""
        return self.side1*self.side2*self.side3

    def __repr__(self) -> str:
        return f"Cube(x = {self.x}, y = {self.y}, z = {self.z}, side1 = {self.side1}, side2 = {self.side2}, side3 = {self.side3})"


class Sphere(Circle):
    """Sphere class, child class of Circle, representing a spherical geometric shape"""    
    def __init__(self, x: float, y: float, z: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.z = z

    @property
    def z(self) -> float:
        return self._z

    @z.setter
    def z(self, value) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f"z must be either int or float, not {type(value).__name__}")
        self._z = value                

    @property
    def area(self) -> float:
        """Area of sphere"""
        return 4*np.pi * self.radius**2

    @property
    def volume(self) -> float:
        """Volume of sphere"""
        return 4/3 * np.pi * self.radius**3

    def __repr__(self) -> str:
        return f"Sphere(x = {self.x}, y = {self.y}, z = {self.z}, radius = {self.radius})"