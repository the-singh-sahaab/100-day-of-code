class Solution:
    def check(self, nums: List[int]) -> bool:
        num1 = sorted(nums)
        for i in range(len(nums)):
            if nums[i:]+nums[:i]==num1:
                return True
        return False

        
        
