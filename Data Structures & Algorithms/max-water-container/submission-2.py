class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute Force: Check all combinations and max areas

        # 2 PTR: max(maxArea, min(l,r)*(r-l))
        # squeze a ptr if next bar is taller
        # O(n)



        n = len(heights)
        l,r=0,n-1
        maxArea = 0

        while l<=r:
            a = min(heights[l],heights[r]) * (r-l)
            maxArea = max(maxArea, a)

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxArea