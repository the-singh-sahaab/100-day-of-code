class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        st_sum = {0: -1}
        Sum = 0
        max_len = 0
        for i in range(len(nums)):
            if nums[i]:
                Sum+=1
            else:
                Sum+=-1
            if st_sum.get(Sum, None)==None:
                st_sum[Sum]=i
            else:
                max_len = max(max_len, i-st_sum[Sum])
        return max_len


        