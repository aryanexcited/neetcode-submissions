"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        starts, ends = [], []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        n = len(intervals)
        ends.sort()
        i = 0
        j = 0
        rooms = 0
        max_rooms = 0
        while i < n and j < n:
            if starts[i] < ends[j]:
                rooms += 1
                i += 1
            else:
                rooms -= 1
                j += 1
            max_rooms = max(max_rooms, rooms)

        return max_rooms