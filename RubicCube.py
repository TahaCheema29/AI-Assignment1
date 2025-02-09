import copy
import stat

from constants import Face,Movement,Color

class RubicCube:
    
    def set_cube(self):
        with open('partB.txt', 'r') as file:
            lines = file.readlines()
        with open('partC.txt', 'w') as file:
            file.write(lines[0])

        initial_cube = lines[0].strip().split(',')

        if len(initial_cube) != 54:  
            raise ValueError("Invalid cube state in file. Expected 54 elements.")

        self.cube = self.convert_list_to_cube(initial_cube)

    @staticmethod
    def convert_list_to_cube(cube_list):
        return {
            Face.UPPER: [cube_list[0:3], cube_list[3:6], cube_list[6:9]],
            Face.FRONT: [cube_list[9:12], cube_list[12:15], cube_list[15:18]],
            Face.RIGHT: [cube_list[18:21], cube_list[21:24], cube_list[24:27]],
            Face.BACK: [cube_list[27:30], cube_list[30:33], cube_list[33:36]],
            Face.LEFT: [cube_list[36:39], cube_list[39:42], cube_list[42:45]],
            Face.DOWN: [cube_list[45:48], cube_list[48:51], cube_list[51:54]],
        }

    def print_cube(self):
        print("\n    " + "\n    ".join(self.print_face(Face.UPPER)))
        for i in range(3):
            print(f"{' '.join(self.cube[Face.LEFT][i])}   "
                  f"{' '.join(self.cube[Face.FRONT][i])}   "
                  f"{' '.join(self.cube[Face.RIGHT][i])}   "
                  f"{' '.join(self.cube[Face.BACK][i])}")
        print("    " + "\n    ".join(self.print_face(Face.DOWN)))

    def print_face(self, face: Face):
        return [' '.join(row) for row in self.cube[face]]

    def read_moves(self):
        with open('partB.txt', 'r') as file:
            lines = file.readlines()

        moves = [line.strip().split(',') for line in lines[1:]]  
        
        for move in moves:
            if len(move) != 2:  
                raise ValueError(f"Invalid move format: {move}. Expected format: FaceID,MoveID.")

        return moves 

    def apply_move(self, face: Face, move: Movement):
        """Apply a move (clockwise or anti-clockwise) to a specific face."""
        if face in {Face.UPPER, Face.DOWN}:
            face_to_change = [Face.BACK, Face.RIGHT, Face.FRONT, Face.LEFT]
            face_to_place = [Face.LEFT, Face.BACK, Face.RIGHT, Face.FRONT] if move == Movement.CLOCKWISE else \
                            [Face.FRONT, Face.RIGHT, Face.BACK, Face.LEFT]
            row = 0 if face == Face.UPPER else 2
            self.move_horizontal(row, face_to_change, face_to_place)

        elif face in {Face.FRONT, Face.BACK}:
            face_to_change = [Face.UPPER, Face.RIGHT, Face.DOWN, Face.LEFT]
            face_to_place = [Face.LEFT, Face.UPPER, Face.RIGHT, Face.DOWN] if move == Movement.CLOCKWISE else \
                            [Face.DOWN, Face.RIGHT, Face.UPPER, Face.LEFT]
            col = 0 if face == Face.FRONT else 2
            self.move_vertical(col, face_to_change, face_to_place)

        elif face == Face.RIGHT:
            face_to_change = [Face.UPPER, Face.BACK, Face.DOWN, Face.FRONT]
            face_to_place = [Face.FRONT, Face.UPPER, Face.BACK, Face.DOWN] if move == Movement.CLOCKWISE else \
                            [Face.DOWN, Face.BACK, Face.UPPER, Face.FRONT]
            col = 2
            self.move_vertical(col, face_to_change, face_to_place)

        elif face == Face.LEFT:
            face_to_change = [Face.UPPER, Face.FRONT, Face.DOWN, Face.BACK]
            face_to_place = [Face.BACK, Face.UPPER, Face.FRONT, Face.DOWN] if move == Movement.CLOCKWISE else \
                            [Face.DOWN, Face.FRONT, Face.UPPER, Face.BACK]
            col = 0
            self.move_vertical(col, face_to_change, face_to_place)

        self.rotate_face(face, move)

    def move_horizontal(self, row: int, face_to_change: list[Face], face_to_place: list[Face]):
        """Shifts a row horizontally across four adjacent faces."""
        temp = self.cube[face_to_place[0]][row]
        for i in range(4):
            self.cube[face_to_change[i]][row], temp = temp, self.cube[face_to_change[i]][row]

    def move_vertical(self, col: int, face_to_change: list[Face], face_to_place: list[Face]):
        """Shifts a column vertically across four adjacent faces."""
        temp = [row[col] for row in self.cube[face_to_place[0]]]
        for i in range(4):
            current_face = face_to_change[i]
            next_temp = [row[col] for row in self.cube[current_face]]
            for j in range(3):
                self.cube[current_face][j][col] = temp[j]
            temp = next_temp

    def rotate_face(self, face: Face, move: Movement):
        """Rotates a face's 3×3 grid 90 degrees (clockwise or anti-clockwise)."""
        temp = copy.deepcopy(self.cube[face])
        if move == Movement.CLOCKWISE:
            for i in range(3):
                for j in range(3):
                    self.cube[face][j][2 - i] = temp[i][j]
        else:  # Anti-clockwise
            for i in range(3):
                for j in range(3):
                    print('i',i)
                    print('j',j)
                    print('face',face)
                    print('self.cube[face]',self.cube[face])
                    self.cube[face][2 - j][i] = temp[i][j]

    def execute_moves(self):
        """Reads moves from the file and applies them sequentially to the cube."""
        moves = self.read_moves()

        for move in moves:
            face = Face(move[0])
            move_type = Movement(move[1])
            self.apply_move(face, move_type)

        print("All moves executed successfully!")

    def write_result_to_file(self):
        """Writes the final cube state to a file in the same format as partB.txt."""
        cube_state = []
        
        for face in [Face.UPPER, Face.FRONT, Face.RIGHT, Face.BACK, Face.LEFT, Face.DOWN]:
            for row in self.cube[face]:
                cube_state.extend(row)

        with open("partB.txt", 'a') as file:
            file.write(",".join(cube_state) + "\n")
        with open("partC.txt", 'a') as file:
            file.write(",".join(cube_state) + "\n")
        
        print(f"Final cube state written to {"partB.txt"}.")
    
    
# from CubeSolver import CubeSolver
# from RubicCube import RubicCube


def main():
    cube = RubicCube()
    cube.set_cube()
    print("Initial Cube State:")
    cube.print_cube()
    cube.execute_moves()
    print("\nFinal Cube State:")
    cube.print_cube()
    cube.write_result_to_file()

    # solver = CubeSolver(cube)
    # solver.compare_algorithms()

if __name__ == "__main__":
    main()
