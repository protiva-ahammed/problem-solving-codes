class Solution:
    def maxArea(self, height: List[int]) -> int:
        reqTarget=0
        left , right = 0,len(height)-1
        while left < right:            
            if height[left]<height[right]:
                area=height[left]*(right-left)
                left +=1
            else:
                area=height[right]*(right-left)
                right-=1
            reqTarget = max(reqTarget,area)
        return max(reqTarget,area)