class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute force: For every i, check proceeding temps
        # O(N*N)

        # Stack: while i is smaller than i-1, stack up
        # When i is greater, check against previous temps

        stack = []
        res = [0] * len(temperatures)
        for idx,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                i = stack.pop()
                res[i] = idx-i
            stack.append(idx)
        return res