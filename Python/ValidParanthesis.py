class Solution:
    def isValid(self, s: str) -> bool:

        complement = {"(": ")", "{":"}", "[":"]"}

        if len(s) == 1:
            return False

        stack = []
        
        for i in s:
            if i in complement:
                stack.append(i)
            elif len(stack) == 0 or i != complement[stack.pop()]:
                return False

        return len(stack) == 0
        
