class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = '0000'
        if target == start:
            return 0

        if start in deadends:
            return -1

        q = deque([start])
        visited = set(deadends)
        visited.add(start)
        moves = 0

        while q:
            moves += 1
            # check at each level
            for _ in range(len(q)):
                combination = q.popleft()
                # move all 4 locks of the combination
                for lock in range(4):
                    # move up and down
                    for j in [1, -1]:
                        digit = str((int(combination[lock]) + j + 10) % 10)
                        newCombination = combination[:lock] + digit + combination[lock+1:]
                        if newCombination in visited:
                            continue
                        if newCombination == target:
                            return moves
                        q.append(newCombination)
                        visited.add(newCombination)
        return -1
