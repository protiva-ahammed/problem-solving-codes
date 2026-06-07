class TimeMap:
#constructor. the first time a new instance (object) of a class is created 
    def __init__(self):
        self.store = {} # dictonary = key: list of pairs [val, timestamp]
        
# alic=key, pair...=[alice]:[ [happy,1 ],[sad,3]..]
    def set(self, key: str, value: str, timestamp: int) -> None: #O(1)
        #  key like alice, mike,wonderland, first value will be [] emptylist
        if key not in self.store: 
            self.store[key] = [] #if the keys not in store then put the key and assign empty val
        # if exists enter values
        # actually self.keyStore = {} is a dictonary. it will now append the values
        self.store[key].append([value, timestamp])
        
#  how could do it better!?
    def get(self, key: str, timestamp: int) -> str: # usualy O(n),O(nlogn) => O(logn) constrains said it is in ASC so dir impl BinSearch
        res=""
        values = self.store.get(key,[])
        # binary search impl
        l,r=0, len(values)-1 # index 0 , n-1
        while l<=r:# r=n-1 so <=
            m = (l+r)//2
            # if timestamp is not exactly than take the prev one
            if values[m][1]<= timestamp:# closest timestamp, can not be max
                res = values[m][0]
                l = m+1
            else:
                r = m-1
        return res

        
        
