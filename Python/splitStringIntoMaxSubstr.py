class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        # we iterate the string from starting index.
        # we recursively split the string into substrings, and maintain a count for it. 
        # we return the max_value of the count.
        # we also remove the substring at the end to make space for other variants

        # check to save computation time
        if len(s) == 1:
            return 1

        def backtrack(idx, seen):
            if idx == len(s):
                return 0
            
            splits = 0

            for end in range(idx + 1, len(s) + 1):
                substring = s[idx: end]
                if substring not in seen:
                    seen.add(substring)
                    splits = max(splits, backtrack(end, seen) + 1)
                    seen.remove(substring)

            return splits
        
        return backtrack(0, set())
