class Solution:
    def isValid(self, s: str) -> bool:
        closed={')':'(','}':'{',']':'['}
        stack = []
        for i in s:
            if stack and i in ")]}":
                peek = stack.pop()
                if peek != closed[i]:
                    return False
            else:
                stack.append(i)
        return len(stack)==0

