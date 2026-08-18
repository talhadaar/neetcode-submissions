class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # BS in one pass
        # Linearized coords
        # start = 0, end = ROWS*COLS-1
        # any one coord, r = i // COLS, c = i % COLS
        l,r = 0, (ROWS*COLS) - 1
        
        while l<=r:
            mid = l+(r-l) // 2
            val = matrix[mid // COLS][mid % COLS]
            if target > val:
                l = mid + 1
            elif target < val:
                r = mid - 1
            else:
                return True

        return False