class Solution:
    def lengthOfLongestSubstring(self, strs: str) -> int:
        subSet = set()
        l=0
        res = 0
        
        for i in range(len(strs)):
            while strs[i] in subSet:
                subSet.remove(strs[l])
                l+=1
            subSet.add(strs[i])
            res = max(res,i-l+1)
        return res
        