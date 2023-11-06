class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        count = 0
        winner = arr[0]
        
        for i in range(1, len(arr)):
            if arr[i] > winner:
                winner = arr[i]
                count = 1
            else:
                count += 1
            
            if count == k:
                return winner
        
        return winner