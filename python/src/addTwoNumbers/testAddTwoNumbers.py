import unittest
from addTwoNumbers import Solution, ListNode

def intToListNode(integer):
    result = ListNode(integer % 10)
    if integer / 10 > 0:
        result.next = intToListNode(integer / 10)
    return result

class TestIntToListNode(unittest.TestCase):
    def test1Is1(self):
        self.assertEqual(intToListNode(1), ListNode(1))

    def test1IsNot10(self):
        notExpected = ListNode(0)
        notExpected.next = ListNode(1)
        self.assertNotEqual(intToListNode(1), notExpected)

    def test10Is10(self):
        expected = ListNode(0)
        expected.next = ListNode(1)
        self.assertEqual(intToListNode(10), expected)

    def test10IsNot11(self):
        notExpected = ListNode(1)
        notExpected.next = ListNode(1)
        self.assertNotEqual(intToListNode(10), notExpected)

    def test10IsNot20(self):
        notExpected = ListNode(0)
        notExpected.next = ListNode(2)
        self.assertNotEqual(intToListNode(10), notExpected)

    def test20Is20(self):
        expected = ListNode(0)
        expected.next = ListNode(2)
        self.assertEqual(intToListNode(20), expected)

    def test765Is765(self):
        expected = ListNode(5)
        expected.next = ListNode(6)
        expected.next.next = ListNode(7)
        self.assertEqual(intToListNode(765), expected)

    def test1000Is1000(self):
        expected = ListNode(0)
        expected.next = ListNode(0)
        expected.next.next = ListNode(0)
        expected.next.next.next = ListNode(1)
        self.assertEqual(intToListNode(1000), expected)

class TestAddTwoNumbers(unittest.TestCase):
    def test1Plus1Is2(self):
        solution = Solution()
        one = intToListNode(1)
        self.assertEqual(solution.addTwoNumbers(one, one), intToListNode(2))

    def test4Plus4Is8(self):
        solution = Solution()
        four = intToListNode(4)
        self.assertEqual(solution.addTwoNumbers(four, four), intToListNode(8))

    def test10Plus10Is20(self):
        solution = Solution()
        ten = intToListNode(10)
        self.assertEqual(solution.addTwoNumbers(ten, ten), intToListNode(20))

    def test111Plus222Is333(self):
        solution = Solution()
        oneOneOne = intToListNode(111)
        twoTwoTwo = intToListNode(222)
        self.assertEqual(solution.addTwoNumbers(oneOneOne, twoTwoTwo), intToListNode(333))

    def test1Plus100Is101(self):
        solution = Solution()
        one = intToListNode(1)
        oneHundred = intToListNode(100)
        self.assertEqual(solution.addTwoNumbers(one, oneHundred), intToListNode(101))

    def test1Plus1000Is1001(self):
        solution = Solution()
        one = intToListNode(1)
        oneThousand = intToListNode(1000)
        self.assertEqual(solution.addTwoNumbers(one, oneThousand), intToListNode(1001))

    def test9Plus1Is10(self):
        solution = Solution()
        nine = intToListNode(9)
        one = intToListNode(1)
        self.assertEqual(solution.addTwoNumbers(nine, one), intToListNode(10))

    def test9Plus9Is18(self):
        solution = Solution()
        nine = intToListNode(9)
        self.assertEqual(solution.addTwoNumbers(nine, nine), intToListNode(18))

    def test99Plus1Is100(self):
        solution = Solution()
        nineNine = intToListNode(99)
        one = intToListNode(1)
        self.assertEqual(solution.addTwoNumbers(nineNine, one), intToListNode(100))

    def test999Plus1Is1000(self):
        solution = Solution()
        nineNineNine = intToListNode(999)
        one = intToListNode(1)
        self.assertEqual(solution.addTwoNumbers(nineNineNine, one), intToListNode(1000))

if __name__ == '__main__':
    unittest.main()
