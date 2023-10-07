class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        else:
            n = 0
            b = 0
            nums  = sorted(nums)
            for i in range(len(nums)-1):
                if b < (nums[i+1]-nums[i]):
                    b = nums[i+1] - nums[i]
            return b