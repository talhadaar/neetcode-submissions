class Solution:
    def trap(self, height: List[int]) -> int:
        # 1 pass instead of multiple
        # Monotonic stack: Assume every next bar is smaller than last
        # if a taller bar is reached, it becomes the right
        # current bar becomes the bottom and the bar before it becomes the left wall
        # We find all such containers in one pass to trap water

        stack = []
        water = 0

        for i,h in enumerate(height):
            # make containers
            while stack and height[stack[-1]] < h:
                bottom = height[stack.pop()]
                if not stack:
                    break
                right = h
                left = height[stack[-1]]
                # area at this bar
                distance = i - stack[-1] - 1
                water += (min(left,right) - bottom) * distance
            stack.append(i)
        return water