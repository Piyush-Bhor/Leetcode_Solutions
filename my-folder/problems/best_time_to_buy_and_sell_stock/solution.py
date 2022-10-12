class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        def stocks(prices):
            l,r = 0,1
            maxP = 0
            while r < len(prices):
                if prices[l] < prices[r]:
                    diff = prices[r] - prices[l]
                    maxP = max(diff, maxP)
                    r += 1
                else:
                    l = r
                    r += 1
            return maxP
        return stocks(prices)