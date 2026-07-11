class Solution:
    def maxArea(self, height: List[int]) -> int:
        reqTarget=0
        left , right = 0,len(height)-1
        while left < right:            
            if height[left]<height[right]:
                reqTarget=max(height[left]*(right-left),reqTarget)
                left +=1
            else:
                reqTarget=max(height[right]*(right-left),reqTarget)
                right-=1
        return reqTarget