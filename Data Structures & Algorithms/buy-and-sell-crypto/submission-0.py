class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]
        # for one index calculate the
        # max amount by interating each index
        for sell in (prices):
            maxP = max(maxP,sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP

        