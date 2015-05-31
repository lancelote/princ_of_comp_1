import unittest

from week1.proj1 import slide, merge


class TestSlide(unittest.TestCase):

    def test_slide_returns_correct_result(self):
        self.assertEqual(slide([1, 0, 1, 1]), [1, 1, 1, 0])
        self.assertEqual(slide([0, 0, 1, 1]), [1, 1, 0, 0])
        self.assertEqual(slide([1, 1, 0, 0]), [1, 1, 0, 0])
        self.assertEqual(slide([0, 0, 0, 0]), [0, 0, 0, 0])
        self.assertEqual(slide([0, 0, 0, 1]), [1, 0, 0, 0])
        self.assertEqual(slide([0, 1]), [1, 0])


class TestMerge(unittest.TestCase):

    def test_merge_returns_correct_result(self):
        self.assertEqual(merge([2, 0, 2, 4]), [4, 4, 0, 0])
        self.assertEqual(merge([0, 0, 2, 2]), [4, 0, 0, 0])
        self.assertEqual(merge([2, 2, 0, 0]), [4, 0, 0, 0])
        self.assertEqual(merge([2, 2, 2, 2]), [4, 4, 0, 0])
        self.assertEqual(merge([8, 16, 16, 8]), [8, 32, 8, 0])
        self.assertEqual(merge([8, 8]), [16, 0])
