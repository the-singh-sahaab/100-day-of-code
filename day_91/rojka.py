class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        res = 1;
        for i in range(0,len(nums)):
            j = bisect.bisect_left(lis,nums[i]);
            if(j<len(lis)): lis[j] = nums[i]
            else:lis.append(nums[i])
            if(len(lis)>res):
                res = len(lis)
        return res   