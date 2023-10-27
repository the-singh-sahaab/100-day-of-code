class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMaxSum=1
        currMinSum=1
        res=nums[0]
        for i in range(0,len(nums)):
            currMaxSum,currMinSum=max(currMaxSum*nums[i],nums[i],currMinSum*nums[i]),min(currMaxSum*nums[i],nums[i],currMinSum*nums[i])
            res=max(res, currMaxSum)
        return res