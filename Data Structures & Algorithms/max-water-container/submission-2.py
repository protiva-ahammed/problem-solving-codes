class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxh=-1
        for i in range(0,len(height)-1):
            for j in range(i+1,len(height)):
                if height[i]>height[j]:
                    area = height[j]*(j-i)
                else:
                    area=height[i]*(j-i)
                if area>maxh:
                    maxh=area  
        return maxh