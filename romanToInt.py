class Solution:
    def romanToInt(self, s: str) -> int:

        romanMap = {"I": 1, "V": 5, "X" : 10, "L" : 50, "C": 100, "D": 500, "M":1000}
        
        f = 0
        i = 0

        while i < len(s) - 1:
            if romanMap[s[i]] < romanMap[s[i + 1]]:
                f -= romanMap[s[i]]
            else:
                f += romanMap[s[i]]
            
            i += 1

        return f + romanMap[s[-1]]
            

        

        
