class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        new = []
        for i in nums:
            new.append(int(str(i)[::-1]))
        # print(nums+new)
        return len(list(set(nums+new)))
        
        