class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        # not brute force
        hashmap = {}
        pairs = 0

        # iterate through rows and append to hashmap
        for row in grid:
            hashmap[tuple(row)] = hashmap.get(tuple(row), 0) + 1

        # iterate through the columns and check if similar row exists in hashmap. If yes, decrement count. 
        for col in zip(*grid):
            pairs += hashmap.get(tuple(col), 0)
            
        return pairs 
