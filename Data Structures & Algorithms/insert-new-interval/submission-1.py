class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Intervals are non-overlapping and sorted by start.
        # We can insert newInterval by comparing ends
        # Binary Search and Insert then merge - O(n)
        # Greedy: Place where possible, merge till possible, let the rest be
        # Either before current interval, or after it or requires merging.
        res = []

        for i in range(len(intervals)):
            # Before current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res+intervals[i:]
            # After current interval, so continue looking
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # must merge
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res