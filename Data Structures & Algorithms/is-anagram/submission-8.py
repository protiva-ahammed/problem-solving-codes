class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        ana = {}
        for i in s:
            ana[i]= ana.get(i,0)+1
        for i in t:
            ana[i]= ana.get(i,0)-1
        for val in ana.values():
            if val != 0:
                return False
        return True


        