class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l ,r = 0 ,len(nums) -1 
        while  l <= r :
            m = (l + r)//2
            if nums[m] == target:
                return m

            #left sorted
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l] :
                    l = m + 1 # we need min
                else :
                    r = m - 1
            #right sorted
            else :
                if target < nums[m] or target > nums[r]:
                    r = m - 1 # left side already larger so min in right side
                else :
                    l = m + 1
        return -1