class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # i = j = 0

        # if s == "":
        #     return True
        
        # if t == "" and s != "":
        #     return False
        

        # while j < len(t):
        #     if s[i] == t[j]:
        #         i += 1
        #     j += 1

        #     if (i == len(s)):
        #         return True

        # return False      

    
        # Method 2

        if s == "":
            return True
        
        if t == "":
            return False
        
        j = 0

        for i in range(len(t)):
            if j < len(s) and s[j] == t[i]:
                j += 1 
           
        
        return j == len(s)
        
        
