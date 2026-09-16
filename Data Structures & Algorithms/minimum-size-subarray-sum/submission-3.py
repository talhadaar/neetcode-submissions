class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        result = float('inf')
        l = 0

        for r in range(n):
            total += nums[r]
            while total >= target:
                result = min(result, r - l + 1)
                total -= nums[l]
                l += 1
        return result if result != float('inf') else 0