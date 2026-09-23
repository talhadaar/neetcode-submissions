class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Leave alone cells at the edges
        # Do DFS from every boundary cell that is 'O'
        R = len(board)
        C = len(board[0])

        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or board[r][c] != 'O':
                return

            board[r][c] = '#'

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(R):
            for c in range(C):
                if r == 0 or r == R - 1 or c == 0 or c == C - 1:
                    dfs(r, c)

        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'