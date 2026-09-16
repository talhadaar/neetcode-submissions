class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Brute force: Find all subarrays and check against target, pick the smallest one
        # O(N^N)

        # Sliding Window variable size: while window is invalid keep expanding
        # Valid because only positive numbers, so increasing size increases sum and vice versa

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