class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Longest strictly increasing subsequence

        # Recursively:
        # At every number, we have a choice: We pick it only if it's larger than the last
        # i.e: What is the longest increasing subsequence starting at any i?

        cache = defaultdict(int)

        def dfs(i, j):
            if i == len(nums):
                return 0

            if cache[(i,j+1)]:
                return cache[(i,j+1)]
            # Skip
            res = dfs(i + 1, j)

            # include if
            # a. just starting out
            # b. nums[i] is increasing
            # result is the consequence of both choices
            if j == -1 or nums[j] < nums[i]:
                res = max(res, 1 + dfs(i + 1, i))

            cache[(i,j+1)] = res
            return res

        return dfs(0, -1)