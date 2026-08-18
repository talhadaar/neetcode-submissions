class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # staircase search: O(M+N) at worst, could give all vertically and horizontally for target

        # Binary Search
        # 2 pass: Narrow and binary search: Find a row that is a suitable rage with BS, search row with BS
        # 1 pass: Linearize coords and do a binary search: Whole thing O(log(n))


        # find a row
        top, bottom = 0, ROWS - 1
        while top < bottom:
            mid = (top + bottom) // 2
            if matrix[mid][-1] < target:
                top = mid + 1
            else:
                bottom = mid
        row = top
        # now we BS on the row
        l,r = 0, COLS - 1
        while l<=r:
            mid =(l+r) // 2
            if target < matrix[row][mid]:
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True
        return False
