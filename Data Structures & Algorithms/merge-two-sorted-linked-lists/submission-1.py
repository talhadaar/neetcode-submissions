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
        newHead = ptr = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next
            ptr = ptr.next

        ptr.next = list1 or list2

        return newHead.next