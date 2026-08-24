# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # # '<' operator
    # def __lt__(self, other) -> bool:
    #     if isinstance(other, ListNode):
    #         if self.val < other.val:
    #             return True
    #         else:
    #             return False
    #     else:
    #         return NotImplemented

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # handle empty lists
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # handle with recursion
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2