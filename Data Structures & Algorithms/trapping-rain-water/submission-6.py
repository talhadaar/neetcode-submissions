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
        # O(N), O(N)

        # 2 Pointers:
        # Move the shorter height side inwards
        # Keep track of max height on either side of the pointers
        # Calculate area between max height on either side and the pointers
        # THis way we calculate area between every bucket on left and right
        # while moving inwards
        # no reason to move pointers backwards, only inwards
        n = len(height)
        l,r = 0,n-1
        leftMax,rightMax = height[l],height[r]
        res = 0

        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                res+= leftMax-height[l]
            else:
                r -=1
                rightMax = max(rightMax, height[r])
                res+=rightMax-height[r]
        return res