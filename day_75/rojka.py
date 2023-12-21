class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [x for x in nums if x > 0]
        nums = sorted(list(set(nums)))
        t = 0
        for i in range(len(nums)):
            t+=1
            if nums[i]!=t:
                return t
        return t+1
        