# Given an array of integers, find two numbers such that they add up to a
# specific target number.
#
# The function twoSum should return indices of the two numbers such that they add
# up to the target, where index1 must be less than index2. Please note that your
# returned answers (both index1 and index2) are not zero-based.
#
# You may assume that each input would have exactly one solution.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        self.num_ = num
        self.target_ = target

        diffDict = self.generateDeltaDict()

        for i, val in enumerate(self.num_):
            if val in diffDict and diffDict[val] is not i:
                i = self.toOneBasedIndex(i)
                j = self.toOneBasedIndex(diffDict[val])
                return (i, j) if i < j else (j, i)

    def generateDeltaDict(self):
        return {self.targetDelta(val): pos for pos, val in enumerate(self.num_)}

    def targetDelta(self, n):
        return self.target_ - n

    def toOneBasedIndex(self, i):
        return i + 1
