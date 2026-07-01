# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # revHead: head of reversed list
        # curr: node whos link is being reversed
        revHead, curr = None, head

        while curr:
            remainingList = curr.next
            # reverse link of curr to point to revHead
            curr.next = revHead
            # update revHead to new head
            revHead = curr
            # update current to remainingList's head for processing
            curr = remainingList
        return revHead