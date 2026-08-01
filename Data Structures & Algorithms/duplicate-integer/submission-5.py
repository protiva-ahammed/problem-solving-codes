class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists = set()
        for i in nums:
            if i in exists:
                return True
            else:
                exists.add(i)
        return False     
        