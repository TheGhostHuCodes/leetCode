import unittest
from twoSum import Solution

class TestTwoSum(unittest.TestCase):
    def testLeetCodeExamplePasses(self):
        solution = Solution()
        numbers = [2, 7, 11, 15]
        target = 9
        self.assertEqual(solution.twoSum(numbers, target), (1, 2))
        
    def testUnorderedList(self):
        solution = Solution()
        numbers = [3, 2, 4]
        target = 6
        self.assertEqual(solution.twoSum(numbers, target), (2, 3))

if __name__ == '__main__':
    unittest.main()
