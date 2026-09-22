class Solution:
    def trap(self, height: List[int]) -> int:
        def scan(h):
            water = 0
            l, n = 0, len(h)

            while l < n:
                r, bucket = l + 1, 0
                while r < n and h[r] < h[l]:
                    bucket += h[l] - h[r]
                    r += 1
                if r == n:
                    return water, l
                water += bucket
                l = r
            return water, n

        left, peak = scan(height)
        remaining, _ = scan(height[peak:][::-1])
        return left + remaining