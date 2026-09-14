class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums)-1,-1,-1):
            tempDp = set()
            for t in dp:
                newT = t+nums[i]
                if newT==target:
                    return True
                tempDp.add(newT)
                tempDp.add(t)
            dp = tempDp
        return False