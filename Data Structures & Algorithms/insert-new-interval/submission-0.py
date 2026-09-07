class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Intervals are non-overlapping and sorted by start.
        # We can insert newInterval by comparing ends

        intervals.append(newInterval)
        intervals.sort(key=lambda pair: pair[0])

        merged = [intervals[0]]

        for sj,ej in intervals:
            si,ei = merged[-1]
            if sj<=ei:
                merged.pop()
                merged.append([min(si,sj), max(ei,ej)])
            else:
                merged.append([sj,ej])
        return merged