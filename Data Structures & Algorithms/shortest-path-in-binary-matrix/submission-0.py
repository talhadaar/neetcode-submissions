class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Can make Diagonal moves, i.e 8 paths
        # Shortest clean path-> many paths, 1 is best
        # BFS: Shortest path in unweighted graph
        # Process level by level, and nodes need to carry distance

        ROWS,COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1]:
            return -1


        nei = [(0, 1), (1, 0), (0, -1), (-1, 0),
                  (1, 1), (-1, -1), (1, -1), (-1, 1)]

        q = deque([(0,0)])
        visited = set((0,0))
        level = 0
        while q:
            level+=1
            for i in range(len(q)):
                r,c= q.popleft()
                if r == ROWS-1 and c == COLS-1:
                    return level

                for dr,dc in nei:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 0 and
                        (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))

        return -1