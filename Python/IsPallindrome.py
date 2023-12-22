class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) == 1:
            return True

        t = ""

        for i in s:
            if i != " " and i.lower() in "0123456789qwertyuioplkjhgfdsazxcvbnm":
                i = i.lower()
                t += i

        return t == t[::-1]

        
