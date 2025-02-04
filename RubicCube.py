import copy
from enum import Enum

class Face(Enum):
    UPPER='U'
    FRONT='F'
    RIGHT='R'
    BACK='B'
    LEFT='L'
    DOWN='D'


class RubicCube:
    
    cube = {
    Face.UPPER: [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],
    Face.FRONT: [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],
    Face.RIGHT: [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],
    Face.BACK: [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],
    Face.LEFT: [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],
    Face.DOWN: [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]}
    
    def __init__(self):
        pass

    def print_cube(self):
        for face in self.cube:
            print(f"{face.name}:\n{self.cube[face]}\n")

    def move_r(self,row:int):
        face_to_change=[Face.RIGHT, Face.BACK, Face.LEFT, Face.FRONT]
        face_to_place=[Face.FRONT, Face.RIGHT, Face.BACK, Face.LEFT]

        next=self.cube[face_to_place[0]][row]
        for i in range(4):
            change_face=face_to_change[i]
            curr=next
            next=self.cube[change_face][row]
            self.cube[change_face][row]=curr
            # print(self.cube[change_face][row])
            # print(next)

    def move_l(self,row:int):
        face_to_change=[Face.BACK, Face.RIGHT, Face.FRONT, Face.LEFT]
        face_to_place=[Face.LEFT, Face.BACK, Face.RIGHT, Face.FRONT]

        next=self.cube[face_to_place[0]][row]
        for i in range(4):
            change_face=face_to_change[i]
            curr=next
            next=self.cube[change_face][row]
            self.cube[change_face][row]=curr

    def move_u(self,col:int):
        face_to_change=[Face.FRONT, Face.UPPER, Face.BACK, Face.DOWN]
        face_to_place=[Face.DOWN, Face.FRONT, Face.UPPER, Face.BACK]

        next=copy.deepcopy(self.cube[face_to_place[0]])
        for i in range(4):
            change_face=face_to_change[i]
            curr=copy.deepcopy(next)
            next=copy.deepcopy(self.cube[change_face])
            for j in range(3):
                print(next)
                self.cube[change_face][j][col]=curr[j][col]

    def move_d(self,col:int):
        face_to_change=[Face.UPPER, Face.FRONT, Face.DOWN, Face.BACK]
        face_to_place=[Face.BACK, Face.UPPER, Face.FRONT, Face.DOWN]

        next=copy.deepcopy(self.cube[face_to_place[0]])
        for i in range(4):
            change_face=face_to_change[i]
            curr=copy.deepcopy(next)
            next=copy.deepcopy(self.cube[change_face])
            for j in range(3):
                print(next)
                self.cube[change_face][j][col]=curr[j][col]


def main():
    cube = RubicCube()
    
    print("Initial Cube State:")
    cube.print_cube()

    print("Applying R move (Right Face Row 0)")
    cube.move_d(0)
    cube.print_cube()



if __name__ == "__main__":
    main()