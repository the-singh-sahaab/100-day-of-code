class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows=[0]*m
        cols=[0]*n
        for i,j in indices:
            rows[i]+=1
            cols[j]+=1
        count=0
        for i in rows:
            for j in cols:
                if (i+j)%2==1:
                    count+=1
        return count
