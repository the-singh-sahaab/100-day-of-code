class Solution:
    def minMoves(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()
        for i in range(len(nums)-1,0,-1):
            diff = nums[i] - nums[0]
            sum = sum + diff
        return sum
        