class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*(n)

        prefix = 0
        for i in range(n):
            res[i] = nums[i]*i - prefix
            prefix += nums[i]

        suffix = 0
        for i in range(n-1,-1,-1):
            res[i] += suffix - nums[i]*(n-1-i)
            suffix += nums[i] 

        return res
        # nu = {}
        # for i in range(len(nums)-1):
        #     a = 0
        #     for j in range(i+1,len(nums)):
        #         if i in nu:
        #             nu[i] += abs(nums[i]-nums[j])
        #         else:
        #             nu[i] = abs(nums[i]-nums[j])
        #         if j in nu:
        #             nu[j] += abs(nums[i]-nums[j])
        #         else:
        #             nu[j] = abs(nums[i]-nums[j])
        # return list(nu.values())