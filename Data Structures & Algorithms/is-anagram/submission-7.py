class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        # ana = {0}
        # # ana2={}
        # for i in s:
        #     ana[i]+=1
        # for i in t:
        #     ana[i]-=1
        
        # return ana == 0
        return Counter(s)== Counter(t)


        