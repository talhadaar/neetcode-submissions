# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def remove(self, head, n):
        if not head:
            return None

        head.next = self.remove(head.next, n)
        n[0] -=1
        if n[0] == 0:
            return head.next
        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return self.remove(head, [n])