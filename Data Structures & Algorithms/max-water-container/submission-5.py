class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Container: any 2 bars min(barA,barB)*width

        # Brute Force: Pick a bar, make a cointainer from remaining bars, check water trapped between them
        # works regardless of what height of bars between the 2 bars were
        # O(N*N)

        # 2 Pointers:
        # Not sorted, so how do we move the pointers? to guarantee meaningfull affect on the are?

        res = 0
        n = len(heights)

        l,r = 0,n-1

        while l<r:
            area = min(heights[l], heights[r]) * (r-l)
            res = max(res, area)

            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return res