# Given an array of integers, every element appears twice except for one. Find
# that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber0(self, A):
        """Solving the problem with sets."""
        uniques = set(A)
        for i in uniques:
            A.remove(i)
        single = set(A) ^ uniques
        return list(single)[0]

    def singleNumber1(self, A):
        """Solving the problem with a dictionary."""
        paired = {}
        for i in A:
            if i not in paired:
                paired[i] = False
            else:
                paired[i] = True
        for key in paired.keys():
            if paired[key] == False:
                return key

    def singleNumber2(self, A):
        """Solving the problem with bit manipulation."""
        result = 0
        for i in A:
            result = result ^ i
        return result

    def singleNumber(self, A):
        """Solving the problem with functional constructs."""
        return reduce(lambda x, y: x^y, A)
