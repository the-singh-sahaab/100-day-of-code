class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        for i in nums:
            if i<0:
                n.append(i)
            else:
                p.append(i)
        ans=[]
        for i,j in zip(p,n):
            ans.append(i)
            ans.append(j)
        return ans