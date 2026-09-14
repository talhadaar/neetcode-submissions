class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        dp = set()
        dp.add(0)

        for num in nums:
            tempDp = set()
            for t in dp:
                newT = t+num
                if newT==target:
                    return True
                if newT < target: tempDp.add(newT)
                tempDp.add(t)
            dp = tempDp
        return False