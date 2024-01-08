class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        one_list = s.split('0')
        zero_list = s.split('1')

        one_max = max(one_list, key=len)
        zero_max = max(zero_list, key=len)

        return len(one_max) > len(zero_max)