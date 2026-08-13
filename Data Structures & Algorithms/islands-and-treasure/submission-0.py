class Solution:
    INF = 2147483647
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        q = deque()
        visited = set()


        # If it a valid unvisited cell, que it for BFS
        def queCell(r,c):
            if (min(r,c)<0 or r == ROWS or c == COLS or (r,c) in visited or grid[r][c]==-1):
                return
            visited.add((r,c))
            q.append((r,c))

        
        # find all treasures and que them
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    q.append((r,c))
                    visited.add((r,c))
        
        # run bfs, processing each level
        level = 0
        while q:
            for i in range(len(q)):
                r0,c0 = q.popleft()
                grid[r0][c0] = level
                for rd,cd in directions:
                    queCell(r0+rd, c0+cd)
            level+=1