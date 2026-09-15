class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])

        # Binary Search and find a target row
        lo,hi = 0, R-1

        while lo<=hi:
            mid = (lo+hi) // 2

            if target < matrix[mid][0]:
                hi = mid - 1
            elif target > matrix[mid][C-1]:
                lo = mid+1
            else:
                break
        else:
            return False

        # now search over the mid row
        r = mid
        lo,hi = 0,C-1

        while lo<=hi:
            mid = (lo+hi) // 2

            if target<matrix[r][mid]:
                hi = mid - 1
            elif target>matrix[r][mid]:
                lo = mid+1
            else:
                return True

        return False