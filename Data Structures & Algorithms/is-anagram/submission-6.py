class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        ana = {}
        ana2={}
        for i in range(len(s)):
            if (s[i] in (ana)):
                ana[s[i]]+=1
            else:
                ana[s[i]]=1

        for i in range(len(t)):
            if(t[i] in (ana2)):
                ana2[t[i]]+=1
            else: ana2[t[i]]=1

        return ana2==ana


        