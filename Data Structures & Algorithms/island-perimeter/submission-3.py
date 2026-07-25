class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        perimeter = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    perimeter+=4
                    # reduce if top is land
                    if r and grid[r-1][c]==1:
                        perimeter-=2
                    # reduce if left is land
                    if c and grid[r][c-1]==1:
                        perimeter-=2
        return perimeter