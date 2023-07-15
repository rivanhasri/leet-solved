class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        import math
        if sorted(prices, reverse=True) == prices:
            return 0
        minimum_price = math.inf
        maximum_price = 0
        for price in prices:
            if price < minimum_price:
                minimum_price = price
            elif maximum_price < price - minimum_price:
                maximum_price = price - minimum_price
        return maximum_price