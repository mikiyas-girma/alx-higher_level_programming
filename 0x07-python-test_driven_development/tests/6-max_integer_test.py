import unittest
import sys
sys.path.append('..')
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """Test that the function returns None for an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        """Test that the function returns the single element for a
        list with one element."""
        self.assertEqual(max_integer([1]), 1)

    def test_multiple_elements(self):
        """Test that the function returns the maximum element
          for a list with multiple elements."""
        self.assertEqual(max_integer([3, 2, 1]), 3)
        self.assertEqual(max_integer([5, -2, 10]), 10)

    def test_negative_elements(self):
        """Test that the function handles lists with negative elements."""
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([-5, 2, -10]), 2)


if __name__ == "__main__":
    unittest.main()
