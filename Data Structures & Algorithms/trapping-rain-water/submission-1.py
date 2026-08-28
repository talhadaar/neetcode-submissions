class Solution:
    def trap(self, height: List[int]) -> int:
        # Return total water trapped in ALL the bars

        # Brute Force:
        # At each i, find leftMax and Right max, to find water i'th bar can trap
        # O(n*n)
        
        # Bit nicer:
        # Precompute Prefix and Suffix of maxL and maxR at each height[i]
        # Compute once, calculate once.
        # O(N), (ON)

        # Stack
        # Push i'th bar to stack till a taller one is seen
        # This means: stack[-1] is the leftWall and stack[0] is right wall
        # Compute distance, height and sum up area

        if not height:
            return 0
        n = len(height)
        res = 0
        stack = []

        # Check for every bar
        for i in range(n):
            # While theres bars in stack(We have potential left walls)
            # and while we've found right walls
            # calculate area on each of the bars on stack
            while stack and height[i]>=height[stack[-1]]:
                mid = height[stack.pop()] # bar bounded by left and right
                # if there's a right wall
                if stack:
                    left = height[stack[-1]]
                    right = height[i]
                    h = min(left, right) - mid # height of bucket
                    w = i - stack[-1] - 1
                    res += h*w
            # append new wall to stack
            stack.append(i)
        return res