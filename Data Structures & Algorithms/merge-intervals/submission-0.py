class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # is intervals sorted? If yes, just merge, if not, sort and merge
        # After sorting, if sj<=ei: then merge. merged[si, max(ei,ej)]

        intervals.sort(key=lambda pair: pair[0])
        res = [intervals[0]]
        
        for sj,ej in intervals:
            ei = res[-1][1]

            if sj<=ei:
                res[-1][1] = max(ei, ej)
            else:
                res.append([sj,ej])
        return res