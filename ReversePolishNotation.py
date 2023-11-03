
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        if tokens[0] in "+-*/":
            return 0

        # KEEP ON ADDING NUMBERS TO STACK
        # IF TOKEN IS ENCOUNTERED, POP LAST 2 ELEMENTS (GUARANTEED TO EXIST) AND PERFORM OPERATION.
        # APPEND ANSWER IN STACK

        for token in tokens :
            if token == '+' :
                a , b = stack.pop() , stack.pop()
                stack.append( a + b ) 
            elif token == '-':
                a , b = stack.pop() , stack.pop()
                stack.append( b - a ) 
            elif token == '*':
                a , b = stack.pop() , stack.pop()
                stack.append( b * a ) 
            elif token == '/':
                a , b = stack.pop() , stack.pop()
                stack.append( int(b / a) ) 
            else:
                stack.append(int(token))

        # RETURN STACK.POP() AND NOT STACK[-1] AS POP() IS FASTER
        return stack.pop()





