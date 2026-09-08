class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute Force: Expand right from every temp[i] till a higher temp is reached
        # O(N*N)

        # Monotonic Stack: Push indeces while a temp more than stack[-1] is reached
        # O(N)
        stack = []
        output = [0] * len(temperatures)
        for idx,temp in enumerate(temperatures):
            while stack and temp>temperatures[stack[-1]]:
                t = stack.pop()
                output[t] = idx-t
            stack.append(idx)
        return output