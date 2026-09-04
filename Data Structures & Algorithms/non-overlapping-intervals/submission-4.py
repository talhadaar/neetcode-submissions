class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # [1, 3] and [2, 4] are overlapping, but [1, 2] and [2, 3] are non-overlapping
        # Continuous intervals are not overlapping.
        # Interval to be removed is: overlapping and non-continuous
        # Overlaps occurs if: sj<ei, we chose to keep the interval with the smaller e and remove the other.
        # Removing one with larger e reduces problem space where overlaps can occur.

        intervals.sort(key=lambda pair:pair[0])

        ei = intervals[0][1]
        count = 0

        for sj,ej in intervals[1:]:
            if sj>=ei:
                ei=ej
            else:
                # overlap happened
                count+=1
                # chose min(ei,ej) to keep
                ei = min(ei,ej)
        return count