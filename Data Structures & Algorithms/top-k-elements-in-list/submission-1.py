class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a map of {num:freq}
        counts = {}

        # O(n)
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        arr = []
        #O(N)
        for num,fq in counts.items():
            arr.append([fq, num])
        arr.sort() # O(?)

        sol = []
        while len(sol) < k:
            sol.append(arr.pop()[1])
        return sol