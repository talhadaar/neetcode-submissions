class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 1 == Land
        # 0 == Water
        # Verticle & Horizontal movements only
        # Island = one or more connected cells
        # Exactly one island
        # NO LAKES
        # Cell side length == 1

        # Find a land cell
        # do BFS on each cell, calculat it's weight
        # Weight of a cell/node = 4 - edges connecting it
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    q.append((r,c))

        perimeter = 0
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            r0,c0 = q.popleft()
            for rd,cd in dirs:
                rn,cn = r0+rd, c0+cd
                if 0 <=rn < ROWS and 0<=cn<COLS:
                    if grid[rn][cn] == 0:
                        # if neighbour is water we have a countable perimeter
                        perimeter+=1
                else:
                    perimeter+=1
        return perimeter