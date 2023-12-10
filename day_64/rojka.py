class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        # brute force
        res = 0
        indices_list = []
        for i in range(len(nums)):
            count_1 = 0
            for c in bin(i):
                if c == '1':
                    count_1 += 1
            if count_1 ==k:
                indices_list.append(i)
        return sum([nums[i] for i in indices_list])