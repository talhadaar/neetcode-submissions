# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        # find middle of LL
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the 2nd half of the list
        curr = slow.next
        prev = slow.next = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # merge
        first, second = head,prev
        while second:
            firsttmp,secondtmp = first.next, second.next
            first.next = second
            second.next = firsttmp
            first,second = firsttmp,secondtmp
    