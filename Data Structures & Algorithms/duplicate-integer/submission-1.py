class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unqSet = set()
        for i in nums:
            unqSet.add(i)
        if len(nums)==len(unqSet):
            return False
        return True
        