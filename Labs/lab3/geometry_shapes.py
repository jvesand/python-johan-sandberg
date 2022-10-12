from __future__ import annotations
import numpy as np

class Shape:
    """Shapes parent class"""
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    # add validation code for x,y
    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value) -> None:
        self._x = value

    # cross shape operator overloads based on area (<, >, <=, >=)
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

    def translate(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"An instance of the {self.__class__.__name__} class: {self.__repr__()}\n" \
            f"The {self.__class__.__name__.lower()} has an area of {self.area} and a circumference of {self.circumference}.\n" \
            f"{self.is_special()}\n"


class Rectangle(Shape):
    """Rectangle"""
    def __init__(self, x, y: float, side1: float, side2: float) -> None:
        super().__init__(x, y)
        self.side1 = side1
        self.side2 = side2

    # add validation code for side1, side2
    @property
    def side1(self) -> float:
        return self._side1

    @side1.setter
    def side1(self, value) -> None:
        self._side1 = value

    @property
    def area(self) -> float:
        return self.side1 * self.side2

    @property
    def circumference(self) -> float:
        return (self.side1 + self.side2) * 2

    def is_special(self) -> str:
        if self.side1 == self.side2:
            return "The rectangle is square."
        else:
            return "The rectangle is not square."

    def is_inside(self, x: float, y: float) -> bool:
        return (self.x - self.side1/2 <= x <= self.x + self.side1/2) and \
            (self.y - self.side2/2 <= y <= self.y + self.side2/2)

    def __eq__(self, other: Rectangle) -> bool:
        """==, evaluates TRUE if two rectangles have the same location and shape"""
        return (self.__class__ == other.__class__ and self.x == other.x and \
            self.y == other.y and self.side1 == other.side1 and self.side2 == other.side2)

    def __repr__(self) -> str:
        return f"Rectangle(x = {self.x}, y = {self.y}, side1 = {self.side1}, side2 = {self.side2})"


class Circle(Shape):
    """Circle"""
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y)
        self.radius = radius

    # add validation code for radius
    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value) -> None:
        self._radius = value

    @property
    def area(self) -> float:
        return np.pi * self.radius**2

    @property
    def circumference(self) -> float:
        return 2 * np.pi * self.radius

    def is_special(self) -> str:
        if self.radius == 1 and self.x == 0 and self.y == 0:
            return "The circle is a unit circle."
        else:
            return "The circle is not a unit circle"

    def __eq__(self, other: Circle) -> bool:
        """==, evaluates TRUE if two circles have the same location and radius"""
        return (self.__class__ == other.__class__ and self.x == other.x and \
            self.y == other.y and self.radius == other.radius)

    def __repr__(self) -> str:
        return f"Circle(x = {self.x}, y = {self.y}, radius = {self.radius})"
