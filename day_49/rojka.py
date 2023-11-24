class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        a = 0
        new = True
        while new == True:
            if len(piles) == 3:
                return a + piles[1]
            else:
                a+=piles[-2]
                piles.pop(-1)
                piles.pop(-2)
                piles.pop(1)
            

        