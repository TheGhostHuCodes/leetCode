# Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle0(self, head):
        """Solving the problem with a visited array: O(n^2) run time and
        O(n) memory."""
        visited = []
        while head is not None:
            if head in visited:
                return True
            visited.append(head)
            head = head.next
        return False 

    def hasCycle1(self, head):
        """Solving the problem iteratively with the tortise and the hare
        pointers: O(n) run time and O(1) memory."""
        if head is None or head.next is None:
            return False

        tortise = head.next
        hare = head.next.next

        while hare is not None and hare.next is not None:
            if tortise == hare:
                return True
            else:
                tortise = tortise.next
                hare = hare.next.next
        return False

    def hasCycle(self, head):
        """Solving the problem recursively with the tortise and the hare
        pointers: O(n) run time and O(1) memory."""
        if head is None or head.next is None:
            return False
        else:
            return self.hasCycleRecurse(head.next, head.next.next)

    def hasCycleRecurse(self, tortise, hare):
        """Used in above recursive solution."""
        if hare is None or hare.next is None:
            return False
        elif tortise == hare:
            return True
        else:
            return self.hasCycleRecurse(tortise.next, hare.next.next)
