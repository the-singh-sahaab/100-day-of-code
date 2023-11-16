class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        for i in range(1 << len(nums[0])):
            # Convert the current number to a binary string of length n
            binary_str = format(i, '0' + str(len(nums[0])) + 'b')
            if binary_str not in nums:
                return binary_str
        