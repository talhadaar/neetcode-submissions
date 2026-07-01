# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        # set newHead to whatever's at the bottom of the call stack
        newHead = head
        # while there's a head.next keep going to bottom of call stack
        if head.next:
            # returns from bottom of call stack
            newHead = self.reverseList(head.next)
            # reverse link of current head
            head.next.next = head
        # break cycle of current head
        head.next = None

        return newHead