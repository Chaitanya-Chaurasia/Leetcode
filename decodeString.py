class Solution:
    def decodeString(self, s: str) -> str:

        if len(s) == 1:
            return s

        stack = []
        
        for i in s:
            if i != "]":
                stack.append(i)
            else:
                # Make a var that will store eeach substring, and we will later concat all 
                # substrings in the stack

                r = ""

                # Keep on adding strings present in one bracket
                while stack[-1] != "[":
                        r += stack.pop()
                stack.pop()
                # Since the number before a bracket can be more than one digit, we 
                # need to check for all digits and add it to a string, and convert
                # that string to int.

                n = ''
                while len(stack) != 0 and stack[-1].isdigit():
                    n += stack.pop()

                print(r, int(n))
                stack.append(r*int(n[::-1]))

        # Join all substrings present in stack
        return ''.join([word[::-1] for word in stack])




        
        
