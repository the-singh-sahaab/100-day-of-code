class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def backtracking(p,n,r):
            if p==0 and n==0:
                ans.append(r)
            elif r[-1]<0:
                for i in range(1,p+1):
                    backtracking(p-i,n,r+[i])
            else:
                for i in range(1,sum(r)+1):
                    backtracking(p,n-i,r+[-i])
        
        for i in range(1,n+1):
            backtracking(n-i,n-1,[i])
        res=[]
        for i in ans:
            x=""
            for j in i:
                if j>0:
                    for k in range(j):
                        x+="("
                else:
                    for k in range(abs(j)):
                        x+=")"
            x+=")"
            res.append(x)
        return res