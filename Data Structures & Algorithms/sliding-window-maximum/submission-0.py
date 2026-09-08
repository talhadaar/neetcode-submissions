class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Stack: If newly included number is greater than last element in the stack, push it

        # Monotonic stack: keep pushing till a larger element is reach
        # then pop everything behind it 

        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output