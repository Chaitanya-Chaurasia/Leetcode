class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        ''' Solution 1 through for loop
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if i + len(needle) - 1 < len(haystack):
                    if haystack[i : i + len(needle)] == needle:
                        return i
        return -1
        '''

        # Using sliding window

        i = 0

        while i < len(haystack):
            
            if haystack[i] == needle[0]:
                if i + len(needle) - 1 < len(haystack):
                    if haystack[i : i + len(needle)] == needle:
                        return i
            
            i += 1

        return -1

        
