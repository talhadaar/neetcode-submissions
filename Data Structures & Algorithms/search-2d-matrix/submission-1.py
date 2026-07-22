class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])
        toprow, bottomrow = 0, rows - 1

        # narrow down to the row where target could be
        while toprow < bottomrow:
            midrow = (toprow + bottomrow) // 2
            if target > matrix[midrow][-1]:
                toprow = midrow + 1
            elif target < matrix[midrow][0]:
                bottomrow = midrow - 1
            else:
                break
        
        # proceede if theres a valid candidate row
        if not (toprow <= bottomrow):
            return False

        midrow = (toprow + bottomrow) // 2
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[midrow][m]:
                l = m + 1
            elif target < matrix[midrow][m]:
                r = m - 1
            else:
                return True
        return False