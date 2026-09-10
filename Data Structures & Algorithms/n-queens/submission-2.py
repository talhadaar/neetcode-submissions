class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.']*n for i in range(n)]

        col = set()
        primaryDiag = set()
        secondaryDiag = set()

        def backtrack(r):
            if r==n:
                cp = ["".join(row) for row in board]
                res.append(cp)
                return

            for c in range(n):
                # Skip placement if any conflict exists
                if c in col or (r+c) in primaryDiag or (r-c) in secondaryDiag:
                    continue

                # Safe placement and record conflicts
                col.add(c)
                primaryDiag.add(r+c)
                secondaryDiag.add(r-c)
                board[r][c]='Q'

                # Try next row
                backtrack(r+1)

                # backtrack
                col.remove(c)
                primaryDiag.remove(r+c)
                secondaryDiag.remove(r-c)
                board[r][c] = '.'

        backtrack(0)
        return res
