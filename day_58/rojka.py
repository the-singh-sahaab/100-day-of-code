class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        maxReach = 0
        minCoins = 0
        i = 0
        
        while maxReach < target:
            if i < len(coins) and coins[i] <= maxReach + 1:
                maxReach += coins[i]
                i += 1
            else:
                minCoins += 1
                maxReach = 2 * maxReach + 1
        
        return minCoins