class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        # logic: for every subexpression, we only need to know one of the values. 
        # if it is true or false, we can calculate the ops in hand.
        # use stack to pop and append wherever necessary
        # append to stack if not ")"
        # if ")", start popping

        stack = []

        for i in expression:
            if i in [",","("]:
                continue
            elif i != ")":
                stack.append(i)
            else:
                has_true, has_false = False, False
                # we don't check if stack[-1] exists because the given expression is valid.
                while (stack[-1] not in ["!", "&", "|"]):
                    top = stack.pop()
                    if top == "t":
                        has_true = True
                    else:
                        has_false = True
                operator = stack.pop()
                if operator == "!":
                    stack.append("t" if not has_true else "f")
                elif operator == "&":
                    stack.append("t" if not has_false else "f")
                else:
                    stack.append("t" if has_true else "f")
        
        return stack[-1] == "t"
