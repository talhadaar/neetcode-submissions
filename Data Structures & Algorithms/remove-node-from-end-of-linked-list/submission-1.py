# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = ListNode(0, head)
        l,r = tmp,head

        # move ptr2 n nodes up, so we're at n distance
        while n>0:
            r = r.next
            n-=1

        # move both pointers up and right will reach the x-1 node to delete
        while r:
            l = l.next
            r = r.next

        # delete the Nth node from the back
        l.next = l.next.next
        return tmp.next