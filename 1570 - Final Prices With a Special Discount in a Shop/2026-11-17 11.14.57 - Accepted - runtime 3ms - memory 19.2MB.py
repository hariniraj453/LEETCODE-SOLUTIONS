class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = []
        
        for i in range(n):
            discount = 0
            # find next j > i where prices[j] <= prices[i]
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            ans.append(prices[i] - discount)
        
        return ans