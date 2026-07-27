class Solution:
    def isValid(self, s: str) -> bool:
        closed ={')':'(','}':'{',']':'['}
        stack=[]
        if len(s)<=1: return False
        for c in s :
            #is it a closed bracket?
            if c in closed:
                # yes then check if the stack has value? yes-> then check the top is 
                if  stack and stack[-1] == closed[c]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(c)
        return True if not stack else False