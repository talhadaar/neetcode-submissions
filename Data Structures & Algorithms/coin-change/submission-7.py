class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        n = len(coins)
        
        def dfs(i, amount):
            if amount == 0:
                return 0
            if amount < 0 or i == n:
                return float('inf')
            if (i, amount) in memo:
                return memo[(i,amount)]
            # Choice 1: take coin at index i (adds 1 coin)
            # Choice 2: skip coin at index i (adds 0 coins)
            res = min(1 + dfs(i, amount - coins[i]), dfs(i + 1, amount))
            memo[(i, amount)] = res
            return res

        ans = dfs(0, amount)

        return ans if ans != float('inf') else -1