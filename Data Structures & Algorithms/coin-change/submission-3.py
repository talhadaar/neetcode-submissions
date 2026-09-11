class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = defaultdict(int)
        coins.sort(reverse=True)

        def dfs(amount):
            # if target reached, no more coins needed
            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]

            res = 1e9
            for coin in coins:
                if amount-coin >=0:
                    res = min(res, 1+dfs(amount-coin))
            memo[amount] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins>=1e9 else minCoins