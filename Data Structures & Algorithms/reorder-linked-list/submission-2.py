# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [0, 1, 2, 3, 4, 5, 6]

# [0, 6, 1, 5, 2, 4, 3]

# [0, n-1, 1, n-2, 2, n-3, ...]

# Half, Reverse, Merge
# [0,1,2,3,4]
# [0, 4, 1, 3, 2]
# [0,1,2], [4,3]
# [0,4,1,3,2]
# O(N+M), O(1)

# Half, Stack, pop and merge
# [0,1,2], stack: [3, 4]
# 0,4,1,3,2
# O(M+N), O(M)

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
            if not head or not head.next:
                return

            def reverse(head):
                prev, curr = None, head
                while curr:
                    t = curr.next
                    curr.next = prev
                    prev = curr
                    curr = t
                return prev

            # Merge ll2 into ll2 in-place
            def merge(ll1, ll2):
                tail = ListNode()
                while ll1 and ll2:
                    tail.next = ll1
                    ll1 = ll1.next
                    tail.next.next = ll2
                    tail = ll2
                    ll2 = ll2.next
                tail.next = ll1 or ll2

            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            second = slow.next
            # Break up to avoid cycle
            slow.next = None
            merge(head, reverse(second))