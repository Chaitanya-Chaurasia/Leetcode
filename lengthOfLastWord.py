class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        s = s.strip()

        l = s.split(" ")

        if len(l) == 1:
            return len(l[0])

        return len(s.split(" ")[-1])
        
        
