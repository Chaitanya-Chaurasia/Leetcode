class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # our approach: two pointers and hashmap
        # store the last occurence of each char in s in a hashmap
        # we iterate and compute end pointer as max(end, hashmap[char])
        # if we are at an index where our current index == end pointer, we have found one partition.
        # we calculate length and add to res.

        hashmap = {char: i for i, char in enumerate(s)}
        res, start, end = [], 0, 0
        for idx, char in enumerate(s):
            end = max(end, hashmap[char])
            if idx == end:
                res.append(idx - start + 1)
                start = end + 1
        return res
