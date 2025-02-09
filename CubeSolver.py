from collections import deque
import copy
import heapq

from RubicCube import RubicCube
from constants import Face, Movement

class CubeSolver:
    def __init__(self, cube: RubicCube):
        self.initial_state = self.load_initial_state()
        self.goal_state = self.load_goal_state()
        self.cube = cube

    def load_initial_state(self):
        with open('partC.txt', 'r') as file:
            lines = file.readlines()
        return lines[0].strip()

    def load_goal_state(self):
        with open('partC.txt', 'r') as file:
            lines = file.readlines()
        return lines[1].strip()

    def bfs_solve(self):
        queue = deque()
        visited = set()
        queue.append((self.initial_state, [], 0))  # (state, path, depth)
        visited.add(self.initial_state)
        
        states_expanded = 0
        max_queue_size = 1

        while queue:
            current_state, path, depth = queue.popleft()
            states_expanded += 1
            max_queue_size = max(max_queue_size, len(queue))

            if current_state == self.goal_state:
                print(f"Solution found in {len(path)} moves!")
                return path, states_expanded, max_queue_size

            for move in self.get_possible_moves():
                new_state = self.apply_move(current_state, move)

                if new_state in visited:    
                    continue 
                
                print('adding in visited ',len(visited))
                print('new state is ',new_state)
                visited.add(new_state)
                queue.append((new_state, path + [move], depth + 1))

        return None, states_expanded, max_queue_size

    def dfs_solve(self):
        stack = [(self.initial_state, [], 0)]  # (state, path, depth)
        visited = set()
        states_expanded = 0
        max_stack_size = 1

        while stack:
            current_state, path, depth = stack.pop()
            states_expanded += 1
            max_stack_size = max(max_stack_size, len(stack))
            
            if current_state == self.goal_state:
                print(f"Solution found in {len(path)} moves!")
                return path, states_expanded, max_stack_size

            if depth < 20:  # Depth limit to prevent infinite recursion
                for move in self.get_possible_moves():
                    new_state = self.apply_move(current_state, move)
                    if new_state not in visited:
                        print('adding in visited ',len(visited))
                        print('new state is ',new_state)
                        visited.add(new_state)
                        stack.append((new_state, path + [move], depth + 1))
        
        return None, states_expanded, max_stack_size

    def a_star_solve(self):
        priority_queue = []
        heapq.heappush(priority_queue, (0, self.initial_state, []))  # (cost, state, path)
        visited = set()
        states_expanded = 0
        max_queue_size = 1
        
        while priority_queue:
            cost, current_state, path = heapq.heappop(priority_queue)
            states_expanded += 1
            max_queue_size = max(max_queue_size, len(priority_queue))
            
            if current_state == self.goal_state:
                print(f"Solution found in {len(path)} moves!")
                return path, states_expanded, max_queue_size

            for move in self.get_possible_moves():
                new_state = self.apply_move(current_state, move)
                if new_state not in visited:
                    print('adding in visited ',len(visited))
                    print('new state is ',new_state)
                    visited.add(new_state)
                    heuristic = self.heuristic(new_state)
                    heapq.heappush(priority_queue, (cost + heuristic, new_state, path + [move]))
        
        return None, states_expanded, max_queue_size

    def heuristic(self, state):
        cube = RubicCube()
        cube.make_cube(state.split(','))

        total_distance = 0
        for piece, correct_pos in zip(state.split(','), self.goal_state.split(',')):
            if piece != correct_pos:
                total_distance += self.manhattan_distance(piece, correct_pos)

        return total_distance

    def manhattan_distance(self, piece, correct_pos):
        """Estimate the number of face rotations needed to move piece to correct position."""
        # Define how pieces move in Rubik’s Cube and estimate cost.
        # Example: If piece is on the opposite face, at least 2 rotations are needed.
        
        face_distance = {
            "U": 0, "D": 0,  # Up and Down require vertical moves
            "L": 1, "R": 1,  # Left and Right require horizontal moves
            "F": 1, "B": 1,  # Front and Back require horizontal moves
        }
        
        piece_face = piece[0]  # Example: "W1" -> "W" (White Face)
        correct_face = correct_pos[0]

        return face_distance.get(piece_face, 2) if piece_face != correct_face else 0

    def apply_move(self, state, move):
        cube = RubicCube()
        cube.make_cube(state.split(','))
        cube.apply_move(move[0], move[1])
        return self.convert_cube_to_string(cube)

    def get_possible_moves(self):
        return [(face, move) for face in Face for move in [Movement.CLOCKWISE, Movement.ANTICLOCKWISE]]

    def convert_cube_to_string(self, cube: RubicCube):
        cube_state = []
        for face in [Face.UPPER, Face.FRONT, Face.RIGHT, Face.BACK, Face.LEFT, Face.DOWN]:
            for row in cube.cube[face]:
                cube_state.extend(row)
        return ",".join(cube_state)

