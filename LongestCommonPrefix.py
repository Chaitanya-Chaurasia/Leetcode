class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1:
            return strs[0]

        strs.sort()

        first = strs[0]
        last = strs[-1]
        lcp = ""

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return lcp
            
            lcp += first[i]

        return lcp

        
        
