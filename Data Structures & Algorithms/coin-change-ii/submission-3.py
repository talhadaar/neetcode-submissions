class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        # Recursively: repick a coin or skip it for the remaining amount
        # Each choice will build a new solution(combination)
        # For any int need between 0 and amount, sum number of coins that form each int
        
        coins.sort()
        cache = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]
        n = len(coins)

        def dfs(i,need):
            # every time need is 0, we found another solution
            if need == 0:
                return 1
            if i >=n:
                return 0

            # if already computed this bit
            if cache[i][need] !=-1:
                return cache[i][need]

            # Keep picking this coin, or more on
            res = 0
            # if this coin and larger can still be used
            if need>=coins[i]:
                # skip this coin and try new solution
                res = dfs(i+1, need)

                # using this coin again for this solution
                res+=dfs(i, need - coins[i])
            cache[i][need] = res
            return res

        return dfs(0, amount)