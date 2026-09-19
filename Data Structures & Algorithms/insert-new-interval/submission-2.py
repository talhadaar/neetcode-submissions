class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Non-overlapping intervals sorted by start
        # Intervals are already non-overlapping
        # So we insert new interval where possible, then merge going forward if possible
        # Search location, insert, then merge
        # Binary Search on start values

        if not intervals:
            return [newInterval]
        
        n = len(intervals)
        target = newInterval[0]
        l,r = 0, n-1

        while l<=r:
            mid = (l+r)//2

            if intervals[mid][0] < target:
                l = mid+1
            else:
                r = mid - 1

        intervals.insert(l, newInterval)

        # now we merge
        res = []
        for interval in intervals:
            # insert if nonoverlapping or empty
            if not res or res[-1][1]<interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res