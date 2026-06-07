class TimeMap:
#constructor. the first time a new instance (object) of a class is created 
    def __init__(self):
        self.keyStore = {} # dictonary = key: list of [val, timestamp] pairs
        
# alic=key, pair...=[alice]:[ [happy,1 ],[sad,3]..]
    def set(self, key: str, value: str, timestamp: int) -> None: #O(1)
        # if the keys not in store enter empty val, like alice, mike,wonderland
        if key not in self.keyStore: 
            self.keyStore[key] = []
        # if exists enter values
        # actually self.keyStore = {} is a dictonary. it will now append the values
        self.keyStore[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str: # usualy O(n),O(nlogn) => O(logn) constrains said it is in ASC so we only can dir impl BinSearch
        res, values = "", self.keyStore.get(key,[])
        # binary search implementations
        l,r=0, len(values)-1 # index 0 , n-1
        while l<=r:
            m = (l+r)//2
            # if timestamp is not exactly than take the prev one
            if values[m][1]<= timestamp:# closest timestamp, can not be max
                res = values[m][0]
                l = m+1
            else:
                r = m-1
        return res

        
        
