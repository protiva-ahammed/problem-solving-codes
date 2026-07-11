class Solution:
    def maxArea(self, height: List[int]) -> int:
        reqTarget=0
        left , right = 0,len(height)-1
        while left < right:
            area = min(height[left],height[right])*(right-left)
            reqTarget=max(area,reqTarget)
            if height[left]<height[right]:
                left +=1
            else:
                right-=1
        return reqTarget