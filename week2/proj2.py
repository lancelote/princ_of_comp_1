# Turn off (bad-builtin) pylint errors:
# pylint: disable=W0141

"""
Clone of 2048 game.
"""

from random import choice

# Uncomment before submitting
# import poc_2048_gui

# Remove or fix before submitting
from week1.proj1 import merge

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

# Replace before submitting or fix import statement
# def merge(line):
#     pass


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.height = grid_height
        self.width = grid_width
        self.grid = []
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for _ in range(2):
            self.new_tile()

    def __str__(self):  # pragma: no cover
        """
        Return a string representation of the grid for debugging.
        """
        return "\n".join([" ".join(map(str, row)) for row in self.grid])

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # Right and Left
        if OFFSETS[direction][0] == 0:
            for i, line in enumerate(self.grid):
                if OFFSETS[direction][1] == 1:
                    self.grid[i] = merge(line)
                else:
                    self.grid[i] = merge(line)[::-1]
        # Up and Down
        else:
            lines = list()
            for line in zip(*self.grid):
                if OFFSETS[direction][0] == 1:
                    lines.append(merge(line))
                else:
                    lines.append(merge(line)[::-1])
            self.grid = list(zip(*lines))

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        population = [4] + [2]*9
        zero_tiles = [(row, col)
                      for row in range(self.height)
                      for col in range(self.width)
                      if self.grid[row][col] == 0]
        row, col = choice(zero_tiles)
        self.grid[row][col] = choice(population)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]

# Uncomment before submitting
# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
