class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        # find rotten and count fresh froots
        rotten = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                if grid[r][c] == 1:
                    fresh+=1

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        mins = 0
        # BFS tym
        # BFS while there's still fresh froot to rott and rotten froont to BFS on
        while fresh > 0 and rotten:
            # we BFS rotten froont on one level in one go
            # min+=1 at it's end
            rottenLen = len(rotten)
            for i in range(rottenLen):
                r0,c0 = rotten.popleft()

                # check each direction of the rott and spread
                for rd,cd in directions:
                    rn,cn = r0+rd, c0+cd
                    # validate coordinate
                    if (0<=rn<ROWS and 0<=cn<COLS):
                        # validate to rott
                        if grid[rn][cn] == 1:
                            grid[rn][cn] = 2
                            fresh-=1
                            rotten.append((rn,cn))
            mins+=1
        if fresh == 0:
            return mins
        else:
            return -1