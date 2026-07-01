# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        rev,curr = None, head

        while curr:
            # backup reversed bit
            prevRev = rev
            # get new node to reverse
            rev = curr
            # move current up to remaining list
            curr = curr.next
            # link new reversed head to previously reversed bit
            rev.next = prevRev
        return rev