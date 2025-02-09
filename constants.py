from enum import Enum


class Face(Enum):
    DOWN = 'D'
    UPPER = 'U'
    FRONT = 'F'
    RIGHT = 'R'
    BACK = 'B'
    LEFT = 'L'

class Movement(Enum):
    ANTICLOCKWISE = 'A'
    CLOCKWISE = 'C'

class Color(Enum):
    WHITE = 'W'
    YELLOW = 'Y'
    ORANGE = 'O'
    RED = 'R'
    GREEN = 'G'
    BLUE = 'B'
