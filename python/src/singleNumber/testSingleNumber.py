import unittest
from singleNumber import Solution

class TestSingleNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testArrayOfSingleIntReturnsOnlyValue(self):
        A = [1]
        self.assertEqual(self.solution.singleNumber(A), 1)

    def testArrayOfTwoTypesOfNumbersReturnsOnlySingleValueNumber(self):
        A = [2, 2, 1]
        self.assertEqual(self.solution.singleNumber(A), 1)

    def testArrayOfThreeTypesOfNumbersReturnsOnlySingleValueNumber(self):
        A = [2, 3, 1, 3, 2]
        self.assertEqual(self.solution.singleNumber(A), 1)

if __name__ == '__main__':
    unittest.main()
