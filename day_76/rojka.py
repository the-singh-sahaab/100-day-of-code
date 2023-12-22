class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        l=len(points)
        print(l)
        s=[]
        for i in range(len(points)):
            s.append(points[i][0])
        s.sort()
        c=0
        for i in range(1,l):
            d=s[i]-s[i-1]
            if(c<d):
                c=d
        return c