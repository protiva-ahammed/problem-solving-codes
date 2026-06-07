# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # len of list 
        n = len(pairs)
        # to store the intermediate state
        res = []
        for i in range(n):
            j = i-1
            # if num[i]>num[i+1] then swap val
            # j>=0 reduce the case for i=0 then j=-1
            while j>=0 and pairs[j].key > pairs[j +1].key:
                pairs[j],pairs[j+1]=pairs[j+1],pairs[j]
                j-=1# means check the initial last value
            res.append(pairs[:])
        return res



        