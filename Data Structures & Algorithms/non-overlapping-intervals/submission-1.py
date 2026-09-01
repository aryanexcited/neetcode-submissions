class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res = []
        count = 0
        for interval in intervals:
            if res and res[-1][1] > interval[0]:
                count+=1
            else:
                res.append(interval)
        return count