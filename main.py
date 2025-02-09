
from CubeSolver import CubeSolver
from RubicCube import RubicCube


def main():
    cube = RubicCube()
    cube.set_cube()
    print("Initial Cube State:")
    cube.print_cube()
    cube.execute_moves()
    print("\nFinal Cube State:")
    cube.print_cube()
    cube.write_result_to_file()

    solver = CubeSolver(cube)
    # print("Solving with BFS...")
    # bfs_solution, bfs_expanded, bfs_queue = solver.bfs_solve()
    # print(f"BFS Solution: {bfs_solution}, States Expanded: {bfs_expanded}, Max Queue Size: {bfs_queue}")
    
    # print("Solving with DFS...")
    # dfs_solution, dfs_expanded, dfs_stack = solver.dfs_solve()
    # print(f"DFS Solution: {dfs_solution}, States Expanded: {dfs_expanded}, Max Stack Size: {dfs_stack}")
    
    print("Solving with A*...")
    a_star_solution, a_star_expanded, a_star_queue = solver.a_star_solve()
    print(f"A* Solution: {a_star_solution}, States Expanded: {a_star_expanded}, Max Queue Size: {a_star_queue}")


if __name__ == "__main__":
    main()
