class Solution:
    def findMin(self, nums: List[int]) -> int:
        l ,r = 0 ,len(nums) -1 
        while  l < r :
            m = l + (r-l)//2
            if nums[m] < nums[r]:
                r = m # we need min
            else : 
                l = m + 1 # left side already larger so min in right side
        return nums[l]      