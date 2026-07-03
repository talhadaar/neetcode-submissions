# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        n1, n2 = l1, l2
        carry, order = 0, 0
        result = ListNode(0)
        dummy = result

        while n1 and n2:
            sum = n1.val + n2.val + carry
            carry = sum // 10
            result.next = ListNode(sum % 10)
            result = result.next
            n1 = n1.next
            n2 = n2.next

        remaining = n1 if n1 else n2
        while remaining:
            sum = remaining.val + carry
            carry = sum // 10
            result.next = ListNode(sum % 10)
            result = result.next
            remaining = remaining.next

        if carry:
            result.next = ListNode(carry)

        return dummy.next
