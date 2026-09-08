class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Area with largest rectangle?
        # Limited by shortest bar in the rectangle
        # area = shortest bar * width
        
        # Brute Force: make all possible subarrays and keep one with max area
        # O(N^N)

        # 2 pointer: no logic to discarcd one side or the other
        # sliding window: same as above, how do I expand or shrink windows?

        # Widest area where any bar can be the shortest
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n + 1):
            while stack and (i == n  or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea