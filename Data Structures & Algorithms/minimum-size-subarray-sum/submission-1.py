class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Brute force: Get subarrays of all size starting from smallest and validate their sums
        # O(N*N), O(1)

        # Prefix array: Calculate prefix array
        # 2 ptrs, expanding from the left
        # expand while convering on target
        # if exceede target, squeeze from left
        # O(2N), O(N)

        # Binary search:
        # If sum of A half is less that target, converge on B half
        # This means we will continue convering until sum >= target
        # for the derived range, check for subarrays

        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i+1] = pre[i] + nums[i]

        best = n + 1
        for i in range(n):
            need = pre[i] + target
            l, r = i + 1, n + 1              # half-open, j can be anything in [i+1, n]
            while l < r:                     # template B: r = mid keeps the candidate
                mid = (l + r) // 2
                if pre[mid] < need: l = mid + 1
                else: r = mid
            if l <= n:                       # l == n+1 means nothing reached need
                best = min(best, l - i)

        return best if best <= n else 0