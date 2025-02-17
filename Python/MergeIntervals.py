class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Our approach: 
        # Start by sorting the list by the lower limit.
        # Now that the list is sorted, we can compare whether to merge or not in a sequential manner.
        # To check if we can merge with the previous "merged" interval, we will keep track of the last interval also.
        # We will check if upper limit of previous interval is GTE lower limit of current interval.
        # Handle whether to add or merge in result list.

        res = []
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]
        for interval in intervals[1: ]:
            if interval[0] <= prev[1]:
                prev[1] = max(interval[1], prev[1])
            else:
                res.append(prev)
                prev = interval
        res.append(prev)
        return res  
