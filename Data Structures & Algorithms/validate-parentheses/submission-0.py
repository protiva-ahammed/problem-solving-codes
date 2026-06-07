class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # a mapping for closing barcket to open bracket
        bracketPatternCloseToOpen  = {")":"(", "}":"{","]":"["}

        for c in s:
            if c in bracketPatternCloseToOpen:
                # stack is not empty & 
                #if top of stack is a close bracket then pop
                if stack and stack [-1] == bracketPatternCloseToOpen[c]:
                    stack.pop()
                # else the string is invalid
                else:
                    return False
            # the bracket is opening bracket then append in stack
            else:
                stack.append(c)
        # after the completion of all operation stack is empty means 
        # all matched so true else false= did not matched
        return True if not stack else False

        