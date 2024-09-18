class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        # do not use += because we are going in reverse order.

        for i in s:
            if i != "]":
                stack.append(i)
            else:
                char = ""
                multiplier = ""

                while stack[-1] != "[":
                    char = stack.pop() + char

                # pop one more time to remove "["
                stack.pop()
                
                # another while loop to get integer since it can be double and triple digits
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier
                
                # compute final string
                char *= int(multiplier)
                stack.append(char)
        
        return "".join(stack)
