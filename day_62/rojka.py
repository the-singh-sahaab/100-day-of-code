
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        d=[1]
        x,y,z=0,0,0
        for i in range(n+1):
          d.append(min(d[x]*2,d[y]*3,d[z]*5))
          m=d[-1]
          if m==d[x]*2:
            x=x+1
          if m==d[y]*3:
            y=y+1
            
          if m==d[z]*5:
            z=z+1
            
        return d[n-1]