class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        s = set()
        while nums:
            uniqueRow = []
            i = 0
            while i < len(nums):
                if nums[i] not in s:
                    s.add(nums[i])
                    uniqueRow.append(nums[i])
                    nums.pop(i)
                    i -= 1 
                i += 1
            ans.append(uniqueRow)
            s.clear()
        return ans