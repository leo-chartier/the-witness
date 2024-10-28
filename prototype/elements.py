from enum import Enum



class Position:
    __x: int
    __y: int

    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x
    
    @property
    def y(self) -> int:
        return self.__y
    
    def __add__(self, other):
        if isinstance(other, Position):
            return Position(self.__x + other.__x, self.__y + other.__y)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Position):
            return Position(self.__x - other.__x, self.__y - other.__y)
        return NotImplemented
    
    def __neg__(self) -> "Position":
        return Position(-self.__x, -self.__y)
    
    def __abs__(self) -> "Position":
        return Position(abs(self.__x), abs(self.__y))
    
    def __repr__(self) -> str:
        return f"({self.__x}, {self.__y})"



class Color(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    # TODO: Find other color values



class IntersectionType(Enum):
    NORMAL = 0
    START = 1
    END = 2
    DOT = 3
    START_SYMMETRY = 4

class EdgeType(Enum):
    NORMAL = 0
    MISSING = 1
    BROKEN = 2
    DOT = 3

class Center:
    pass

class CenterColor(Center):
    color: Color

    def __init__(self, color: Color) -> None:
        super().__init__()
        self.color = color

class CenterTetris(Center):
    shape: list[Position]
    rotatable: bool
    negative: bool

    def __init__(self, shape: list[Position], rotatable: bool = False, negative: bool = False) -> None:
        super().__init__()
        self.shape = shape
        self.rotatable = rotatable
        self.negative = negative

class CenterSun(Center):
    color: Color

    def __init__(self, color: Color) -> None:
        super().__init__()
        self.color = color

class CenterElimination(Center):
    pass

class CenterTriangle(Center):
    number: int

    def __init__(self, number: int) -> None:
        if number < 1 or number > 3:
            raise ValueError("A cell can only have between 1 and 3 triangles")

        super().__init__()
        self.number = number



class Move(Enum):
    UP = Position(0, -1)
    DOWN = Position(0, 1)
    LEFT = Position(-1, 0)
    RIGHT = Position(1, 0)
