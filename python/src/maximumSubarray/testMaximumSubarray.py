import unittest
from maximumSubarray import Solution

class TestMaximumSubarrayEdgeCases(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testEmptyArrayReturnsZero(self):
        self.assertRaises(ValueError, self.solution.maxSubArray, [])

    def testArrayWithSingleEntryReturnsEntry(self):
        self.assertEqual(self.solution.maxSubArray([-1,]), -1)
        self.assertEqual(self.solution.maxSubArray([0,]), 0)
        self.assertEqual(self.solution.maxSubArray([1,]), 1)

class TestMaximumSubarrayWithExamples(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testArrayWithAllNegativeNumbersReturnsLeastNegative(self):
        testArray = [-6, -5, -2, -4, -3]
        self.assertEqual(self.solution.maxSubArray(testArray), max(testArray))

    def testArrayWithAllPositiveNumbersReturnsSumOfWholeArray(self):
        testArray = [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.solution.maxSubArray(testArray), sum(testArray))

    def testArrayWithNegativeNumbersAndZeroReturnsZero(self):
        testArray = [-6, -5, 0, -4, -3, -2]
        self.assertEqual(self.solution.maxSubArray(testArray), max(testArray))

    def testProblemExampleReturns6(self):
        testArray = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(self.solution.maxSubArray(testArray), 6)

if __name__ == '__main__':
    unittest.main()
