import unittest

from mergesort import mergesort


class MyTestCase(unittest.TestCase):
    def test_sorting(self):
        a = [99, 88, 77, 33, 11]  # Arrange
        result = mergesort(a)  # Act
        self.assertEqual([11,33,77,88,99], result)  # Assert

    def test_sorting_long(self):
        a = [99, 88, 77, 33, 11, 65, 22, 43]  # Arrange
        result = mergesort(a)  # Act
        self.assertEqual([11,33,77,88,99], result)
