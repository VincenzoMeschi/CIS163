from maxcont import max_contiguous
import unittest


class TestMaxContiguous(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_contiguous([]), 0)

    def test_single_element_list(self):
        self.assertEqual(max_contiguous([5]), 5)

    def test_positive_numbers(self):
        self.assertEqual(max_contiguous([1, 2, 3, 4]), 10)
        self.assertEqual(max_contiguous([1, 2, -4, 1, 2]), 3)
        self.assertEqual(max_contiguous([1, 2, -4, 1, 2, 6, -3, 5]), 11)

    def test_negative_numbers(self):
        self.assertEqual(max_contiguous([-1, -2, -3, -4]), -1)
        self.assertEqual(max_contiguous([-1, -2, -4, -1, -2]), -1)
        self.assertEqual(max_contiguous([-1, -2, -4, -1, -2, -6, -3, -5]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_contiguous([1, -2, 3, -4, 5, -6, 7]), 7)
        self.assertEqual(max_contiguous([-2, -3, 4, -1, -2, 1, 5, -3]), 7)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_contiguous("not a list")

    def test_unmutated_list(self):
        lst = [1, 2, 3, 4]
        max_contiguous(lst)
        self.assertEqual(lst, [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
