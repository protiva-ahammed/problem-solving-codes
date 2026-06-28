class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = -sys.maxsize
        i=0
        j=1
        while j < len(prices):
            if prices[i] > prices[j]:
                i=j
            else:
                profit = max(profit,prices[j]-prices[i])
            j+=1
        return max(profit,0)
        