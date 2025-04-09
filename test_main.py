import unittest
from main import Solution

class TestFindDisappearedNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(
            self.solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]),
            [5,6]
        )

    def test_empty_array(self):
        self.assertEqual(
            self.solution.findDisappearedNumbers([]),
            []
        )

    def test_all_present(self):
        self.assertEqual(
            self.solution.findDisappearedNumbers([1,2,3,4,5]),
            []
        )

    def test_all_missing(self):
        self.assertEqual(
            self.solution.findDisappearedNumbers([2,2,2,2]),
            [1,3,4]
        )

    def test_duplicates_only(self):
        self.assertEqual(
            self.solution.findDisappearedNumbers([1,1]),
            [2]
        )

if __name__ == '__main__':
    unittest.main()
