class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Traversal: DFS, mark visited stuff in place
        # # of runs will be number of islands

        R = len(grid)
        C = len(grid[0])

        def dfs(r,c):
            if min(r,c)<0 or r>=R or c>=C or grid[r][c]=='0':
                return

            grid[r][c] = '0'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    dfs(r,c)
                    res+=1
        return res
