class Solution:
    def distinctPrimeFactors(self, N: List[int]) -> int:
        h = []
        for n in N:
            i=1
            while(i<=n):
                k=0
                if(n%i==0):
                    j=1
                    while(j<=i):
                        if(i%j==0):
                            k=k+1
                        j=j+1
                    if(k==2):
                        h.append(i)
                i=i+1
        return len(set(h))
        