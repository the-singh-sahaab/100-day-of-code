class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q=[x for x in range(n) ]
        position=0
        while(len(q)>1):
            position=(position+k-1)%len(q) 
            q.pop(position )           
        return q[0]+1