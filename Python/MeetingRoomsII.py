"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        map = defaultdict(int)
        for i in intervals:
            map[i.start] += 1
            map[i.end] -= 1

        prev, res = 0, 0
        for i in sorted(map.keys()):
            prev += map[i]
            res = max(prev, res)
        return res  
