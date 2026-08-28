class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Min height * number of taller bars
        # Can it be a square?

        # Brute Force: find buckets. Expand bucket till a shorter height is seen
        # Calculate area of this bucket
        # O(n*n)

        # Stack(Monotonic):
        # continue stacking as long as bars are taller or equal
        # max(stack) <- left bound
        # min(stack) <- rightBound <-height of rectangle
        # len(stack) <- width
        # No bar to right of heights[-1] so it gets dropped(could be max rectagle), so use 1 extra virtual bar of h 0

        maxArea = 0
        n = len(heights)
        stack = []

        for i in range(n+1):
            # either runs empty
            # or we're dealing with virtual bar
            # or we've reached end of our bucket
            # process the area
            while stack and (i==n or heights[stack[-1]]>=heights[i]):
                height = heights[stack.pop()] # min element at da top
                # If stack was empty, we at i==0 or i==n
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height*width)
            stack.append(i)

        return maxArea