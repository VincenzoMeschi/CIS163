from llstack import LLStack


class InvalidCoordinateError(Exception):
    pass


class Maze:
    """
    Maze class to store maze and solve it.

    Attributes
    ----------
    __nrows : int
        Number of cells wide the maze is.
    __ncols : int
        Number of cells tall the maze is.
    __entry : tuple
        Indices of the entry point of the maze in the form (row, col).
    __exit : tuple
        Indices of the exit point of the maze in the form (row, col).
    __grid : List[List[str]]
        Underlying grid storing the maze. Spots with a 'o' are open and spots with an 'x' are walls.
    __path : LLStack
        Path through the maze.
    __shortest_path : LLStack
        Shortest path through the maze.
    """

    def __init__(self, grid: list, entry_loc: tuple, exit_loc: tuple):
        """
        Constructor for Maze.

        Parameters
        ----------
        grid : List[List[str]]
            Underlying grid storing the maze.
        entry_loc : tuple
            Indices of the entry point of the maze in the form (row, col).
        exit_loc : tuple
            Indices of the exit point of the maze in the form (row, col).
        """

        # grid max dimensions is 3x3

        if len(grid) < 3 or len(grid[0]) < 3:
            raise ValueError("Grid must be at least 3x3.")

        if not isinstance(grid, list) or not all(isinstance(row, list) for row in grid):
            raise TypeError("Grid must be a list of lists.")
        if not isinstance(entry_loc, tuple) or not all(
            isinstance(i, int) for i in entry_loc
        ):
            raise TypeError("Entry coordinates must be a tuple containing integers.")
        if not isinstance(exit_loc, tuple) or not all(
            isinstance(i, int) for i in exit_loc
        ):
            raise TypeError("Exit coordinates must be a tuple containing integers.")
        if (
            entry_loc[0] < 0
            or entry_loc[0] >= len(grid)
            or entry_loc[1] < 0
            or entry_loc[1] >= len(grid[0])
            or grid[entry_loc[0]][entry_loc[1]] == "x"
        ):
            raise InvalidCoordinateError("Invalid entry coordinates.")
        if (
            exit_loc[0] < 0
            or exit_loc[0] >= len(grid)
            or exit_loc[1] < 0
            or exit_loc[1] >= len(grid[0])
            or grid[exit_loc[0]][exit_loc[1]] == "x"
        ):
            raise InvalidCoordinateError("Invalid exit coordinates.")
        
        for row in grid:
            for cell in row:
                if not isinstance(cell, str):
                    raise TypeError

        self.__nrows = len(grid)
        if grid:
            self.__ncols = len(grid[0])
        else:
            self.__ncols = 0
        self.__entry = entry_loc
        self.__exit = exit_loc
        self.__grid = grid
        self.__path = None
        self.__shortest_path = None
        self.__history = set()

    @property
    def nrows(self) -> int:
        """
        Number of cells wide the maze is.

        Returns
        ----------
        int
            Number of cells wide the maze is.
        """

        return self.__nrows

    @nrows.setter
    def nrows(self, value: int):
        """
        Setter for number of cells wide the maze is.

        Parameters
        ----------
        value : int
            Number of cells wide the maze is.
        """

        if value < 3:
            raise ValueError("Number of rows must be at least 3.")
        self.__nrows = value

    @property
    def ncols(self) -> int:
        """
        Number of cells tall the maze is.

        Returns
        ----------
        int
            Number of cells tall the maze is.
        """

        return self.__ncols

    @ncols.setter
    def ncols(self, value: int):
        """
        Setter for number of cells tall the maze is.

        Parameters
        ----------
        value : int
            Number of cells tall the maze is.
        """

        if value < 3:
            raise ValueError("Number of columns must be at least 3.")
        self.__ncols = value

    @property
    def entry_coords(self) -> tuple:
        """
        Indices of the entry point of the maze.

        Returns
        ----------
        tuple
            Indices of the entry point of the maze in the form (row, col).
        """

        return self.__entry

    @entry_coords.setter
    def entry_coords(self, value: tuple):
        """
        Setter for indices of the entry point of the maze.

        Parameters
        ----------
        value : tuple
            Indices of the entry point of the maze in the form (row, col).
        """

        if not isinstance(value, tuple) or not all(isinstance(i, int) for i in value):
            raise TypeError("Entry coordinates must be a tuple containing integers.")
        if (
            value[0] < 0
            or value[0] >= self.__nrows
            or value[1] < 0
            or value[1] >= self.__ncols
            or self.__grid[value[0]][value[1]] == "x"
        ):
            raise InvalidCoordinateError("Invalid entry coordinates.")
        self.__entry = value

    @property
    def exit_coords(self) -> tuple:
        """
        Indices of the exit point of the maze.

        Returns
        ----------
        tuple
            Indices of the exit point of the maze in the form (row, col).
        """

        return self.__exit

    @exit_coords.setter
    def exit_coords(self, value: tuple):
        """
        Setter for indices of the exit point of the maze.

        Parameters
        ----------
        value : tuple
            Indices of the exit point of the maze in the form (row, col).
        """

        if not isinstance(value, tuple) or not all(isinstance(i, int) for i in value):
            raise TypeError("Exit coordinates must be a tuple containing integers.")
        if (
            value[0] < 0
            or value[0] >= self.__nrows
            or value[1] < 0
            or value[1] >= self.__ncols
            or self.__grid[value[0]][value[1]] == "x"
        ):
            raise InvalidCoordinateError("Invalid exit coordinates.")
        self.__exit = value

    @property
    def path(self) -> LLStack:
        """
        Path through the maze.

        Returns
        ----------
        LLStack
            Path through the maze.
        """

        return self.__path

    @property
    def shortest_path(self) -> LLStack:
        """
        Shortest path through the maze.

        Returns
        ----------
        LLStack
            Shortest path through the maze.
        """

        return self.__shortest_path

    def solve(self):
        """
        Top level method to solve the maze.

        If the maze has a solution, after calling this, __path should be updated to be an LLStack representing the valid path through the maze (with the exit cell being the node at the top of the stack and the entry cell being the node at the bottom of the stack).
        If the maze is not solveable, __path should continue to be None after calling this method.

        This method should not use any loops.
        """

        self.__path = LLStack()
        if self.__solve_helper(self.__entry):
            # manually reverse the stack
            temp = LLStack()
            while self.__path.size > 0:
                temp.push(self.__path.pop())
            self.__path = temp
        else:
            self.__path = None

    def __solve_helper(self, loc: tuple):
        """
        Recursive helper method to solve a maze.

        Parameters
        ----------
        loc : tuple
            Current location in the maze.
        """

        # Base case: if we are at the exit, we have solved the maze
        if loc == self.__exit:
            self.__path.push(loc)
            return True

        # Base case: if we have already visited this location, we cannot go here
        if loc in self.__history:
            return False

        # Add this location to the history
        self.__history.add(loc)

        # Recursive cases: try to move in all four directions
        row, col = loc
        if row > 0 and self.__grid[row - 1][col] == "o":
            if self.__solve_helper((row - 1, col)):
                self.__path.push(loc)
                return True
        if row < self.__nrows - 1 and self.__grid[row + 1][col] == "o":
            if self.__solve_helper((row + 1, col)):
                self.__path.push(loc)
                return True
        if col > 0 and self.__grid[row][col - 1] == "o":
            if self.__solve_helper((row, col - 1)):
                self.__path.push(loc)
                return True
        if col < self.__ncols - 1 and self.__grid[row][col + 1] == "o":
            if self.__solve_helper((row, col + 1)):
                self.__path.push(loc)
                return True

        return False


    def solve_shortest(self):
        """
        This method combines the helper methods to create the shortest path possible on the maze
        """
        # Dictionary for memoization
        memo = {}

        # Clear the history set
        self.__history.clear()

        # Find the shortest path
        shortest_length = self.__shortest_path_helper(self.entry_coords, memo)

        # If the shortest path is infinity, there is no path
        if shortest_length == float("inf"):
            self.__shortest_path = None
        else:
            self.__shortest_path = LLStack()
            # Push the entry spot to the shortest path
            self.__shortest_path.push(self.entry_coords)
            self.__make_shortest_path(self.entry_coords, shortest_length, memo)
            self.__shortest_path.push(self.exit_coords)

    def __shortest_path_helper(self, coords, memo):
        """
        This method finds the shortest coordinates and populates them into the memoization dictionary
        :param coords: current set of coords
        :param memo: current version of the memoization dictionary
        """

        # Base case: if the coords are the exit, return 0
        if coords == self.exit_coords:
            return 0

        # Base case: if the coords are out of bounds or are a wall, return infinity
        row, col = coords
        if (
            not (0 <= row < self.__nrows and 0 <= col < self.__ncols)
            or self.__grid[row][col] == "x"
        ):
            return float("inf")

        # Base case: if the coords are in the memoization dictionary, return the value
        if coords in memo:
            return memo[coords]

        # Base case: if the coords are in the history set, return infinity
        if coords in self.__history:
            return float("inf")

        # Add the coords to the history set
        self.__history.add(coords)

        # Recursive cases: try to move in all four directions
        first = self.__shortest_path_helper((row - 1, col), memo)
        second = self.__shortest_path_helper((row + 1, col), memo)
        third = self.__shortest_path_helper((row, col - 1), memo)
        fourth = self.__shortest_path_helper((row, col + 1), memo)

        # Find the shortest path
        shortest = min(first, second, third, fourth) + 1

        # Add the shortest path to the memoization dictionary
        memo[coords] = shortest

        # Remove the coords from the history set
        return shortest

    def __make_shortest_path(self, coords, length, memo):
        row, col = coords
        # Check upward movement
        if self.__path_helper(row - 1, col, length, memo):
            return True
        # Check downward movement
        elif self.__path_helper(row + 1, col, length, memo):
            return True
        # Check leftward movement
        elif self.__path_helper(row, col - 1, length, memo):
            return True
        # Check rightward movement
        elif self.__path_helper(row, col + 1, length, memo):
            return True
        # If none of the directions work, return False
        return False

    def __path_helper(self, next_row, next_col, length, memo):
        if (next_row, next_col) in memo and memo[(next_row, next_col)] == length - 1:
            self.__shortest_path.push((next_row, next_col))
            self.__make_shortest_path((next_row, next_col), length - 1, memo)
            return True
        return False