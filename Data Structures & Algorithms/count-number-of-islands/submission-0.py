class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [(-1,0), (1,0),(0,-1),(0,1)]
        islands= 0
        # find a bit of land
        # do DFS on it to make a path/island
        # mark visited as x

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    islands+=1
                    # dfs tym - Each successful run is 1 island
                    # we mark the land as visited upon deque
                    q = deque([(i,j)])
                    while q:
                        (r0,c0) = q.pop()
                        # mark visited
                        grid[r0][c0] = '0'
                        for rd,cd in dirs:
                            rn,cn = r0+rd,c0+cd
                            if 0<= rn < ROWS and 0<= cn < COLS and grid[rn][cn] == '1':
                                q.append((rn,cn))
        return islands