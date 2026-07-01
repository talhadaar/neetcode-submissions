# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = dict()
        seen = head

        while seen:
            if visited.get(id(seen)):
                return True
            visited[id(seen)] = 1
            seen = seen.next
        return False