class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        n = len(nums)
        res = []
        terms = {}
        cnt = 0 
        for i in range(n):
            res.append(nums[i] - int(str(nums[i])[::-1]))#making res
        for i in res:
            if i not in terms:
                terms[i] = 1
            else :
                cnt+=terms[i]
                terms[i]+=1
        return cnt % (10**9 + 7)
