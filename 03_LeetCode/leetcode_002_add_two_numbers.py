# LeetCode #2: Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        Add two numbers represented by linked lists.
        Each node contains a single digit.
        The digits are stored in reverse order.
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry
            carry = val // 10
            curr.next = ListNode(val % 10)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

# Example test (optional)
# You can run small test cases here to check locally
if __name__ == "__main__":
    # 342 + 465 = 807
    a = ListNode(2, ListNode(4, ListNode(3)))
    b = ListNode(5, ListNode(6, ListNode(4)))
    result = Solution().addTwoNumbers(a, b)

    # print the result
    while result:
        print(result.val, end=" -> " if result.next else "\n")
        result = result.next