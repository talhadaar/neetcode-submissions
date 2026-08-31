# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Recursively: Find k groups all the way to the end
        # Reverse and return it's head

        node, count = head, 0
        while node and count<k:
            node=node.next
            count+=1

        if count<k:
            return head # return non-k groups untouched

        prev = self.reverseKGroup(node, k) # Go all the way to head of last k or non-k group
        curr=head
        while count:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            count-=1
        # prev becomes the head of reversed group, i.e 1->2->3 becomes 3->2->1
        return prev