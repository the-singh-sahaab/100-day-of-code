class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        median = nums[len(nums) // 2]
        for num in nums:
            ans += abs(median - num)
        return ans
        