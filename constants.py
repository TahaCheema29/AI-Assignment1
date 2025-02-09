from enum import Enum


class Face(Enum):
    UPPER = 'U'
    FRONT = 'F'
    RIGHT = 'R'
    BACK = 'B'
    LEFT = 'L'
    DOWN = 'D'

class Movement(Enum):
    ANTI_CLOCKWISE = 'A'
    CLOCKWISE = 'C'

class Color(Enum):
    WHITE = 'W'
    YELLOW = 'Y'
    ORANGE = 'O'
    RED = 'R'
    GREEN = 'G'
    BLUE = 'B'
