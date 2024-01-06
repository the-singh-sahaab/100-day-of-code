class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            l = sorted(set(nums))
            m = 0
            for i in l:
                if nums.count(i) > 1:
                    m += 1
            return m
        else:
            nums = sorted(set(nums))
            m = 0
            min = 0
            max = len(nums)-1
            while min < max:
                midle = (min + max)//2
                if nums[midle] - nums[min] <=k:
                    for i in nums[midle:max+1]:
                        if i - nums[min] == k:
                            m += 1
                            break
                    min += 1
                    max = len(nums)-1
                else:
                    max = midle
            return m