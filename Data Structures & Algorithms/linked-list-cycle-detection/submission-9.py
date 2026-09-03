# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow,fast = head,head
        # If fast.next == None, there was no cycle and traversal is finished
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True

        return False