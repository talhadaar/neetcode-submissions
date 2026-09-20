class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # BFS
        # Imagine 'amount' as starting node
        # coins are it's neighbours
        # find the shortest path from 0 to amount

        if amount==0:
            return 0

        q = deque([0])
        seen = [False] * (amount+1)
        seen[0] = True
        res = 0

        while q:
            # Shortest path: Level where amount was found away from 0
            res +=1
            # process level by level
            for _ in range(len(q)):
                curr = q.popleft()
                # visit neighbours
                for coin in coins:
                    nxt = curr+coin
                    if nxt == amount:
                        return res
                    if nxt>amount or seen[nxt]:
                        continue
                    seen[nxt] = True
                    q.append(nxt)
        return -1