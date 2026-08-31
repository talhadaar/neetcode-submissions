# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Iteratively
        # Comfirm k group in place
        # backup remaining
        # reverse k group
        # attack remaining
        # reverse remaining
        # 4 pointers:
        # curr: Head of current group we're reversing
        # kth: tail of current groug we're reversing
        # gprev: curr -1'th node
        # gnext: kth+1'th node
        # after reversal(curr,kth) we use gprev and gnext to stitch the LL together

        dummy = ListNode(0, head)
        gprev = dummy

        while True:
            # confirm k group
            kth = gprev
            for _ in range(k):
                kth = kth.next
                # no k group at all so return unchanged
                if not kth:
                    return dummy.next

            gnext = kth.next

            # seed the reversal
            prev, curr = gnext, gprev.next
            # reverse k - Normal reversal of a LL of len 
            for _ in range(k):
                tmp = curr.next # backup remaining
                curr.next = prev
                prev = curr
                curr = tmp

            # stitck together reversed bit with the rest
            # i.e: for: 3->2->1->4->5->6: tail=gprev.next=1, gprev.next=kth.next=3, gprev=tail=1
            tail = gprev.next
            gprev.next = kth
            gprev = tail

        return dummy.next