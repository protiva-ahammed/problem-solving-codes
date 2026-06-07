class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference=[]
        for i in range(len(nums)):
            difference = target-nums[i]
            if(difference in nums):
                j = nums.index(difference)
                if i != j:
                    return sorted([i, j])