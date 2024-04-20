class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()
        i = 0
        k = len(piles) - 2
        total = 0
        while(i < k):  
            total += piles[k]
            i += 1
            k -= 2
        return total
                        
        
