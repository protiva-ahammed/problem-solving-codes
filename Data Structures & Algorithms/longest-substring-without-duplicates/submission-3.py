class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        for i in range(0,len(s)):
            seen=set()
            for j in range(i,len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                maxlen=max(maxlen,j-i+ 1)
        return maxlen