
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
    solver.compare_algorithms()

if __name__ == "__main__":
    main()
