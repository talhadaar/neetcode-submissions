class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Can only go down and right
        # Unique paths to reach bottom right corner?

        # Ways to reach any cell[m][n] = cell[m-1][n] cell[m][n-1]

        # Recursively DFS: Follow down or right path, all paths explored are unique ones
        grid = [[-1]*n for i in range(m)]

        def dfs(i,j):
            if i == m-1 and j==n-1:
                return 1

            if i >= m or j >= n:
                return 0

            if grid[i][j] != -1:
                return grid[i][j]

            grid[i][j] =  dfs(i+1,j) + dfs(i,j+1)
            return grid[i][j]

        return dfs(0,0)