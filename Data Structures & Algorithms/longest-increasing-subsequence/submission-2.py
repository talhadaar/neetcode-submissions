class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Longest strictly increasing subsequence

        # Recursively:
        # At every number, we have a choice: Skip it or include it if valid
        # on the rewind: add up the length, take max of both choices
        # i.e: What is the longest increasing subsequence starting at any i?

        # Alternatively:
        # At each i, start finding a subsequence
        # Algo: find next number greater than i at j, do 1+dfs(j)
        # recursively find the subsequence and return with the length
        # do dfs() for all i in the array
        
        n = len(nums)
        memo = [-1]*n


        def dfs(i):
            if memo[i] != -1:
                return memo[i]

            res = 1
            for j in range(i+1, n):
                if nums[i]<nums[j]:
                    res = max(res, 1+dfs(j))

            memo[i] = res
            return res

        return max(dfs(i) for i in range(n))