class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unqSet = set()
        for i in nums:
            unqSet.add(i)
        return len(nums)!=len(unqSet)
            
        