# You are given two linked lists representing two non-negative numbers. The
# digits are stored in reverse order and each of their nodes contain a single
# digit. Add the two numbers and return it as a linked list.
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.val is other.val:
                if self.next is None and other.next is None:
                    return True
                else:
                    return self.next.__eq__(other.next)
            else:
                return False
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        return self.add(l1, l2, 0)

    def add(self, l1, l2, carry):
        if l1 is not None and l2 is not None:
            tempSum = l1.val + l2.val + carry
            result = ListNode(tempSum % 10)
            result.next = self.add(l1.next, l2.next, tempSum / 10)
            return result
        elif l1 is not None:
            tempSum = l1.val + carry
            result = ListNode(tempSum % 10)
            result.next = self.add(l1.next, None, tempSum / 10)
            return result
        elif l2 is not None:
            tempSum = l2.val + carry
            result = ListNode(tempSum % 10)
            result.next = self.add(None, l2.next, tempSum / 10)
            return result
        elif carry is not 0:
            return ListNode(carry)
        else:
            return None
