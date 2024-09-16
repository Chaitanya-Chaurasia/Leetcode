class Solution:
    def removeStars(self, s: str) -> str:

        # Iterate through the string and push to stack until * appears.
        # start popping the stack then.
        # convert list to string using join
        
        stack = []

        for i in s:
            if i != "*":
                stack.append(i)

            elif stack[-1]:
                stack.pop()
                
        
        return "".join(stack)
        
