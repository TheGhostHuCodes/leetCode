# Find the contiguous subarray within an array (containing at least one number)
# which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4], the contiguous subarray
# [4,-1,2,1] has the largest sum = 6.
#
# More practice: If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more subtle.
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A:
            raise ValueError("Array must contain at least one number.")
        if all(map(lambda x: x <= 0, A)):
            return max(A)
        globalMax = 0
        maxSoFar = 0
        for i in A:
            maxSoFar = maxSoFar + i
            if maxSoFar > globalMax:
                globalMax = maxSoFar
            if maxSoFar <= 0:
                maxSoFar = 0
        return globalMax
