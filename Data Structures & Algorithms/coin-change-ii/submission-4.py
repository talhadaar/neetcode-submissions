class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Count how many combinations of coins can make amount.

        # DFS: Chose or skip the coin, test all possibilities, return 1 when amount is reached
        # Sub problem: How many ways to reach a if x ways reached amount?
        n = len(coins)
        cache = {}
        def dfs(i, need):
            if (i,need) in cache:
                return cache[(i,need)]


            if need == 0:
                return 1

            if need < 0 or i >= n:
                return 0

            cache[(i,need)] = dfs(i, need-coins[i]) + dfs(i+1, need)
            return cache[(i,need)]

        return dfs(0, amount)