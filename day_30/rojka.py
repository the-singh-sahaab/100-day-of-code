class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = permutations(nums)
        return perm