class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Divide and Conqure
        # BS problem: for half array, max sum is either left or right half or sum of both(Array is all positives)

        def bs(l,r):
            if l > r:
                return float('-inf')

            mid = (l+r) >> 1
            leftMax = rightMax = currSum = 0
            # Sum left half
            for i in range(mid-1, l-1,-1):
                currSum+=nums[i]
                leftMax = max(leftMax, currSum)

            # Sum right half
            currSum = 0 # reset,reuse,ecece
            for i in range(mid+1,r+1):
                currSum+=nums[i]
                rightMax = max(rightMax, currSum)

            return (max(bs(l, mid-1), bs(mid+1, r), leftMax+nums[mid]+rightMax))

        return bs(0, len(nums)-1)