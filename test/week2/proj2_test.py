# Turn off (too-many-instance-attributes), (invalid-name) and
# (missing-docstring) pylint errors:
# pylint: disable=R0902,C0103,C0111


import unittest
from week2.proj2 import TwentyFortyEight


class TestTwentyFortyEight(unittest.TestCase):

    def setUp(self):
        self.game_square = TwentyFortyEight(4, 4)
        self.game_rectangle = TwentyFortyEight(3, 5)
        self.game_square.reset()
        self.game_rectangle.reset()

    def test_get_grid_height(self):
        self.assertEqual(self.game_square.get_grid_height(), 4)
        self.assertEqual(self.game_rectangle.get_grid_height(), 3)

    def test_get_grid_width(self):
        self.assertEqual(self.game_square.get_grid_width(), 4)
        self.assertEqual(self.game_rectangle.get_grid_width(), 5)

    def test_init(self):
        self.assertEqual(self.game_square.get_grid_height(), 4)
        self.assertEqual(self.game_square.get_grid_width(), 4)
        self.assertEqual(self.game_rectangle.get_grid_height(), 3)
        self.assertEqual(self.game_rectangle.get_grid_width(), 5)

    def test_reset(self):
        # Check length and width
        self.assertEqual(len(self.game_square.grid), 4)
        self.assertTrue(
            all(len(row) == 4 for row in self.game_square.grid)
        )
        self.assertEqual(len(self.game_rectangle.grid), 3)
        self.assertTrue(
            all(len(row) == 5 for row in self.game_rectangle.grid)
        )

        # Check number of zeros
        self.assertEqual(
            sum(n == 0 for row in self.game_square.grid for n in row),
            4*4 - 2
        )
        self.assertEqual(
            sum(n == 0 for row in self.game_rectangle.grid for n in row),
            3*5 - 2
        )

    def test_get_tile(self):
        self.assertEqual(
            self.game_square.get_tile(0, 0),
            self.game_square.grid[0][0]
        )
        self.assertEqual(
            self.game_square.get_tile(3, 3),
            self.game_square.grid[3][3]
        )
        self.assertEqual(
            self.game_rectangle.get_tile(0, 0),
            self.game_rectangle.grid[0][0]
        )
        self.assertEqual(
            self.game_rectangle.get_tile(2, 4),
            self.game_rectangle.grid[2][4]
        )

    def test_set_tile(self):
        self.game_square.set_tile(0, 0, 1)
        self.game_rectangle.set_tile(0, 0, 1)

        self.assertEqual(self.game_square.get_tile(0, 0), 1)
        self.assertEqual(self.game_rectangle.get_tile(0, 0), 1)
