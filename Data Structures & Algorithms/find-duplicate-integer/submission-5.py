class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1<=nums[i]<=n
        # len(nums)==n+1
        # if len(num)==5, then max(nums)==4 and min(nums)==1
        # [1,2,3,4,4]
        # One 1 integer can repeat more than once

        # [1,2,3,3,4] len(5), so 1<=nums[i]<=4

        n = len(nums) - 1
        # Sort and check if nums[i]<=nums[i-1]==nums[i]
        # O(nLog(n)), O(1)

        # O(N) - slow and fast ptr that cycle through till a repitition is hit

        idx = 0
        slow, fast= 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            # if values at 2 indexes brought us to the same location
            # we found the cycle
            if slow==fast:
                break

        # now we need to find what brought us into a cycle - i.e, head of the cycle
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow