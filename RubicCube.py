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
    
    def __init__(self):
        self.cube = {
            Face.UPPER: [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],
            Face.FRONT: [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],
            Face.RIGHT: [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],
            Face.BACK: [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],
            Face.LEFT: [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],
            Face.DOWN: [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]}
    

    def print_cube(self):
        upper = self.print_face(Face.UPPER,self.cube)
        front = self.print_face(Face.FRONT,self.cube)
        right = self.print_face(Face.RIGHT,self.cube)
        back = self.print_face(Face.BACK,self.cube)
        left = self.print_face(Face.LEFT,self.cube)
        down = self.print_face(Face.DOWN,self.cube)
        
        print("    " + upper[0])
        print("    " + upper[1])
        print("    " + upper[2])
        
        for i in range(3):
            print(f"{left[i]}   {front[i]}   {right[i]}   {back[i]}")
        
        print("    " + down[0])
        print("    " + down[1])
        print("    " + down[2])


    @staticmethod
    def print_face(face:str, cube:dict[Face, list[list[str]]]):
        return [' '.join(row) for row in cube[face]]


    @staticmethod
    def move_horizontal(row:int,cube:dict[Face, list[list[str]]],face_to_change:list[Face],face_to_place:list[Face]):
        next=cube[face_to_place[0]][row]
        for i in range(4):
            change_face=face_to_change[i]
            curr=next
            next=cube[change_face][row]
            cube[change_face][row]=curr


    @staticmethod
    def move_vertical(col:int,cube:dict[Face, list[list[str]]],face_to_change:list[Face],face_to_place:list[Face]):
        next=copy.deepcopy(cube[face_to_place[0]])
        for i in range(4):
            change_face=face_to_change[i]
            curr=copy.deepcopy(next)
            next=copy.deepcopy(cube[change_face])
            for j in range(3):
                print(next)
                cube[change_face][j][col]=curr[j][col]


    def move(self,index:int,direction:str):
        if direction==Face.RIGHT:
            face_to_change=[Face.RIGHT, Face.BACK, Face.LEFT, Face.FRONT]
            face_to_place=[Face.FRONT, Face.RIGHT, Face.BACK, Face.LEFT]
            self.move_horizontal(index,self.cube,face_to_change,face_to_place)
        elif direction==Face.LEFT:
            face_to_change=[Face.BACK, Face.RIGHT, Face.FRONT, Face.LEFT]
            face_to_place=[Face.LEFT, Face.BACK, Face.RIGHT, Face.FRONT]
            self.move_horizontal(index,self.cube,face_to_change,face_to_place)
        elif direction==Face.UPPER:
            face_to_change=[Face.FRONT, Face.UPPER, Face.BACK, Face.DOWN]
            face_to_place=[Face.DOWN, Face.FRONT, Face.UPPER, Face.BACK]
            self.move_vertical(index,self.cube,face_to_change,face_to_place)
        elif direction==Face.DOWN:
            face_to_change=[Face.UPPER, Face.FRONT, Face.DOWN, Face.BACK]
            face_to_place=[Face.BACK, Face.UPPER, Face.FRONT, Face.DOWN]
            self.move_vertical(index,self.cube,face_to_change,face_to_place)


def main():
    cube = RubicCube()
    
    print("Initial Cube State:")
    cube.print_cube()

    print("Applying R move (Right Face Row 0)")
    cube.move(2, Face.LEFT)
    cube.print_cube()



if __name__ == "__main__":
    main()