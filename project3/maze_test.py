import unittest
from maze import Maze, InvalidCoordinateError
from llstack import LLStack


class TestLLStack(unittest.TestCase):
    def test_init(self):
        stack = LLStack()
        self.assertEqual(stack.size, 0)

    def test_size(self):
        stack = LLStack()
        stack.push((1, 2))
        stack.push((3, 4))
        self.assertEqual(stack.size, 2)

    def test_pop(self):
        stack = LLStack()
        stack.push((1, 2))
        stack.push((3, 4))
        self.assertEqual(stack.pop(), (3, 4))
        self.assertEqual(stack.size, 1)

    def test_pop_empty(self):
        stack = LLStack()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_push(self):
        stack = LLStack()
        stack.push((1, 2))
        self.assertEqual(stack.size, 1)

    def test_push_invalid(self):
        stack = LLStack()
        with self.assertRaises(TypeError):
            stack.push(1)

    def test_str(self):
        stack = LLStack()
        stack.push((1, 2))
        stack.push((3, 4))
        self.assertEqual(str(stack), "(3,4) -> (1,2)")
    
class TestMaze(unittest.TestCase):
    # Valid grid must be 3x3 minimum.

    def test_init(self):
        grid = [
            ["o", "x", "o"],
            ["o", "x", "o"],
            ["o", "o", "o"],
        ]
        entry = (0, 0)
        exit = (2, 2)
        maze = Maze(grid, entry, exit)
        self.assertEqual(maze.nrows, 3)
        self.assertEqual(maze.ncols, 3)
        self.assertEqual(maze.entry_coords, (0, 0))
        self.assertEqual(maze.exit_coords, (2, 2))
        self.assertEqual(maze.path, None)
        self.assertEqual(maze.shortest_path, None)

    def test_init_invalid_grid(self):
        grid = "invalid"
        entry = (0, 0)
        exit = (2, 2)
        with self.assertRaises(ValueError):
            Maze(grid, entry, exit)

    def test_init_invalid_entry(self):
        grid = [
            ["o", "x", "o"],
            ["o", "x", "o"],
            ["o", "o", "o"],
        ]
        entry = "invalid"
        exit = (2, 2)
        with self.assertRaises(TypeError):
            Maze(grid, entry, exit)

    def test_init_invalid_exit(self):
        grid = [
            ["o", "x", "o"],
            ["o", "x", "o"],
            ["o", "o", "o"],
        ]
        entry = (0, 0)
        exit = "invalid"
        with self.assertRaises(TypeError):
            Maze(grid, entry, exit)

    def test_init_invalid_entry_coords(self):
        grid = [
            ["o", "x", "o"],
            ["o", "x", "o"],
            ["o", "o", "o"],
        ]
        entry = (1, 1)
        exit = (2, 2)
        with self.assertRaises(InvalidCoordinateError):
            Maze(grid, entry, exit)

    def test_init_invalid_exit_coords(self):
        grid = [
            ["o", "x", "o"],
            ["o", "x", "o"],
            ["o", "o", "o"],
        ]
        entry = (0, 0)
        exit = (1, 1)
        with self.assertRaises(InvalidCoordinateError):
            Maze(grid, entry, exit)

    def test_nrows(self):
        grid = [
            ["o", "x", "o"],
            ["o", "x", "o"],
            ["o", "o", "o"],
        ]
        entry = (0, 0)
        exit = (2, 2)
        maze = Maze(grid, entry, exit)
        maze.nrows = 4
        self.assertEqual(maze.nrows, 4)

    def test_nrows_invalid(self):
        grid = [
            ["o", "x", "o"],
            ["o", "x", "o"],
            ["o", "o", "o"],
        ]
        entry = (0, 0)
        exit = (2, 2)
        maze = Maze(grid, entry, exit)
        with self.assertRaises(ValueError):
            maze.nrows = 2

    def test_ncols(self):
        grid = [
            ["o", "x", "o"],
            ["o", "x", "o"],
            ["o", "o", "o"],
        ]
        entry = (0, 0)
        exit = (2, 2)
        maze = Maze(grid, entry, exit)
        maze.ncols = 4
        self.assertEqual(maze.ncols, 4)

    def test_ncols_invalid(self):
        grid = [
            ["o", "x", "o"],
            ["o", "x", "o"],
            ["o", "o", "o"],
        ]
        entry = (0, 0)
        exit = (2, 2)
        maze = Maze(grid, entry, exit)
        with self.assertRaises(ValueError):
            maze.ncols = 2

    def test_entry_coords(self):
        grid = [
            ["o", "x", "o"],
            ["o", "x", "o"],
            ["o", "o", "o"],
        ]
        entry = (0, 0)
        exit = (2, 2)
        maze = Maze(grid, entry, exit)
        maze.entry_coords = (0, 2)
        self.assertEqual(maze.entry_coords, (0, 2))

    def test_entry_coords_invalid(self):
        grid = [
            ["o", "x", "o"],
            ["o", "x", "o"],
            ["o", "o", "o"],
        ]
        entry = (0, 0)
        exit = (2, 2)
        maze = Maze(grid, entry, exit)
        with self.assertRaises(InvalidCoordinateError):
            maze.entry_coords = (1, 1)

    def test_entry_coords_invalid_coords(self):
        grid = [
            ["o", "x", "o"],
            ["o", "x", "o"],
            ["o", "o", "o"],
        ]
        entry = (0, 0)
        exit = (2, 2)
        maze = Maze(grid, entry, exit)
        with self.assertRaises(InvalidCoordinateError):
            maze.entry_coords = (1, 1)

    def test_exit_coords(self):
        grid = [
            ["o", "x", "o"],
            ["o", "x", "o"],
            ["o", "o", "o"],
        ]
        entry = (0, 0)
        exit = (2, 2)
        maze = Maze(grid, entry, exit)
        maze.exit_coords = (1, 2)
        self.assertEqual(maze.exit_coords, (1, 2))

    def test_exit_coords_invalid(self):
        grid = [
            ["o", "x", "o"],
            ["o", "x", "o"],
            ["o", "o", "o"],
        ]
        entry = (0, 0)
        exit = (2, 2)
        maze = Maze(grid, entry, exit)
        with self.assertRaises(InvalidCoordinateError):
            maze.exit_coords = (1, 1)

    def test_exit_coords_invalid_coords(self):
        grid = [
            ["o", "x", "o"],
            ["o", "x", "o"],
            ["o", "o", "o"],
        ]
        entry = (0, 0)
        exit = (2, 2)
        maze = Maze(grid, entry, exit)
        with self.assertRaises(InvalidCoordinateError):
            maze.exit_coords = (0, 1)

    def test_solve(self):
        grid = [
            ["o", "x", "o"],
            ["o", "x", "o"],
            ["o", "o", "o"],
        ]
        entry = (0, 0)
        exit = (2, 2)
        maze = Maze(grid, entry, exit)
        maze.solve()
        self.assertEqual(maze.path.size, 5)
        self.assertEqual(maze.path.pop(), (2, 2))
        self.assertEqual(maze.path.pop(), (2, 1))
        self.assertEqual(maze.path.pop(), (2, 0))
        self.assertEqual(maze.path.pop(), (1, 0))
        self.assertEqual(maze.path.pop(), (0, 0))

    def test_solve_no_solution(self):
        grid = [
            ["o", "x", "o"],
            ["o", "x", "o"],
            ["o", "x", "o"],
        ]
        entry = (0, 0)
        exit = (2, 2)
        maze = Maze(grid, entry, exit)
        maze.solve()
        self.assertEqual(maze.path, None)

    def test_solve_shortest(self):
        grid = [
            ["o", "x", "o"],
            ["o", "x", "o"],
            ["o", "o", "o"],
        ]
        entry = (0, 0)
        exit = (2, 2)
        maze = Maze(grid, entry, exit)
        maze.solve_shortest()
        self.assertEqual(maze.shortest_path.size, 3)
        self.assertEqual(maze.shortest_path.pop(), (2, 2))
        self.assertEqual(maze.shortest_path.pop(), (1, 2))
        self.assertEqual(maze.shortest_path.pop(), (0, 2))

    def test_solve_shortest_no_solution(self):
        grid = [
            ["o", "x", "o"],
            ["o", "x", "o"],
            ["o", "x", "o"],
        ]
        entry = (0, 0)
        exit = (2, 2)
        maze = Maze(grid, entry, exit)
        maze.solve_shortest()
        self.assertEqual(maze.shortest_path, None)


if __name__ == "__main__":
    unittest.main()
