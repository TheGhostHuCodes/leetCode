import unittest
from linkedListCycle import Solution, ListNode

class TestLinkedListCycle(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testNoNodeReturnsFalse(self):
        self.assertEqual(self.solution.hasCycle(None), False)

class TestLinkedListCycleWithList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.head = ListNode(42)

    def testSingleNodeReturnsFalse(self):
        self.assertEqual(self.solution.hasCycle(self.head), False)

    def testTwoNodesReturnsFalse(self):
        node2 = ListNode(43)
        self.head.next = node2
        self.assertEqual(self.solution.hasCycle(self.head), False)

    def testThreeNodesReturnsFalse(self):
        node2 = ListNode(43)
        self.head.next = node2
        node3 = ListNode(44)
        node2.next = node3
        self.assertEqual(self.solution.hasCycle(self.head), False)

    def testTwoNodesInATwoCycleReturnsTrue(self):
        node2 = ListNode(43)
        self.head.next = node2
        node2.next = self.head
        self.assertEqual(self.solution.hasCycle(self.head), True)

    def testThreeNodesInAThreeCycleReturnsTrue(self):
        node2 = ListNode(43)
        self.head.next = node2
        node3 = ListNode(44)
        node2.next = node3
        node3.next = self.head
        self.assertEqual(self.solution.hasCycle(self.head), True)

    def testFourNodesInAThreeCycleReturnsTrue(self):
        node2 = ListNode(43)
        self.head.next = node2
        node3 = ListNode(44)
        node2.next = node3
        node4 = ListNode(45)
        node3.next = node4
        node4.next = node2
        self.assertEqual(self.solution.hasCycle(self.head), True)

    def testFourNodesInAFourCycleReturnsTrue(self):
        node2 = ListNode(43)
        self.head.next = node2
        node3 = ListNode(44)
        node2.next = node3
        node4 = ListNode(45)
        node3.next = node4
        node4.next = self.head
        self.assertEqual(self.solution.hasCycle(self.head), True)

if __name__ == '__main__':
    unittest.main()
