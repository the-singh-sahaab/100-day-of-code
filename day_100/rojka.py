class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count = {}
        for win,loss in matches:
            count[win] = count.get(win,0)
            count[loss] = count.get(loss,0)+1
        
        win = [i for i in count if count[i]==0]
        loss = [i for i in count if count[i]==1]

        return [sorted(win),sorted(loss)]
