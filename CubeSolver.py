import time
from queue import Queue, PriorityQueue
from RubicCube import RubicCube
from constants import Face, Movement

class CubeSolver:
    def __init__(self, cube: RubicCube):
        self.initial_state = self.load_inital_state()
        self.goal_state = self.load_goal_state()
        self.cube = cube
        self.moves = [(face, move) for face in Face for move in Movement]  # Possible face moves

    def load_inital_state(self):
        with open('partC.txt', 'r') as file:
            lines = file.readlines()
        return self.convert_to_tuple(lines[0].strip().split(','))

    def load_goal_state(self):
        with open('partC.txt', 'r') as file:
            lines = file.readlines()
        return self.convert_to_tuple(lines[1].strip().split(','))

    def convert_to_tuple(self, flat_list):
        """Converts a list of 54 elements into a hashable tuple representation."""
        return tuple(flat_list)

    def is_goal_state(self, state):
        """Checks if the given cube state matches the goal state."""
        return state == self.goal_state

    def generate_next_states(self, state):
        """Generates all possible next states efficiently."""
        next_states = []
        for face, move in self.moves:
            new_cube = RubicCube()  # Create a new cube object
            new_cube.cube = new_cube.convert_list_to_cube(list(state))  # Convert tuple back to list for modification
            print('new_cube.cube',new_cube.cube)
            print('face',face)
            print('move',move)
            new_cube.apply_move(face, move)
            next_states.append((tuple(new_cube.cube), (face, move)))  # Convert back to tuple
        return next_states

    def bfs(self):
        """Optimized BFS implementation."""
        start_time = time.time()
        queue = Queue()
        queue.put((self.initial_state, []))  
        visited = {self.initial_state}

        num_expanded = 0
        max_queue_size = 1

        while not queue.empty():
            max_queue_size = max(max_queue_size, queue.qsize())
            current_state, moves = queue.get()
            num_expanded += 1

            if self.is_goal_state(current_state):
                return moves, num_expanded, max_queue_size, time.time() - start_time

            for new_state, move in self.generate_next_states(current_state):
                if new_state not in visited:
                    visited.add(new_state)
                    queue.put((new_state, moves + [move]))

        return None, num_expanded, max_queue_size, time.time() - start_time  # No solution found

    def ids(self, max_depth=20):
        """Optimized Iterative Deepening Search."""
        start_time = time.time()

        def dfs(state, moves, depth):
            nonlocal num_expanded, max_stack_size
            if self.is_goal_state(state):
                return moves
            if depth == 0:
                return None
            num_expanded += 1
            max_stack_size = max(max_stack_size, len(moves))
            for new_state, move in self.generate_next_states(state):
                result = dfs(new_state, moves + [move], depth - 1)
                if result:
                    return result
            return None

        num_expanded = 0
        max_stack_size = 1
        for depth in range(max_depth):
            result = dfs(self.initial_state, [], depth)
            if result:
                return result, num_expanded, max_stack_size, time.time() - start_time

        return None, num_expanded, max_stack_size, time.time() - start_time  # No solution found

    def heuristic(self, state):
        """Improved A* heuristic (misplaced tiles + Manhattan distance)."""
        misplaced = sum(1 for i in range(54) if state[i] != self.goal_state[i])
        return misplaced  # Can be extended with Manhattan distance

    def a_star(self):
        """Optimized A* Search with improved heuristic."""
        start_time = time.time()
        priority_queue = PriorityQueue()
        priority_queue.put((self.heuristic(self.initial_state), 0, self.initial_state, []))  
        visited = {self.initial_state}

        num_expanded = 0
        max_queue_size = 1

        while not priority_queue.empty():
            max_queue_size = max(max_queue_size, priority_queue.qsize())
            _, cost, current_state, moves = priority_queue.get()
            num_expanded += 1

            if self.is_goal_state(current_state):
                return moves, num_expanded, max_queue_size, time.time() - start_time

            for new_state, move in self.generate_next_states(current_state):
                if new_state not in visited:
                    visited.add(new_state)
                    priority_queue.put((self.heuristic(new_state) + cost + 1, cost + 1, new_state, moves + [move]))

        return None, num_expanded, max_queue_size, time.time() - start_time  # No solution found

    def compare_algorithms(self):
        """Compares the performance of BFS, IDS, and A*."""
        print("\nRunning BFS...")
        bfs_result = self.bfs()
        print(f"BFS - Moves: {len(bfs_result[0]) if bfs_result[0] else 'No Solution'}, States Expanded: {bfs_result[1]}, Max Queue Size: {bfs_result[2]}, Time: {bfs_result[3]:.4f}s")

        # print("\nRunning IDS...")
        # ids_result = self.ids()
        # print(f"IDS - Moves: {len(ids_result[0]) if ids_result[0] else 'No Solution'}, States Expanded: {ids_result[1]}, Max Stack Size: {ids_result[2]}, Time: {ids_result[3]:.4f}s")

        # print("\nRunning A*...")
        # a_star_result = self.a_star()
        # print(f"A* - Moves: {len(a_star_result[0]) if a_star_result[0] else 'No Solution'}, States Expanded: {a_star_result[1]}, Max Queue Size: {a_star_result[2]}, Time: {a_star_result[3]:.4f}s")

       