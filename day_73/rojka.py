class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        i=1
        if num==0:
            return True
        while i<num:
            a=str(i)
            a=a[::-1]
            a=int(a)
            if a+i==num:
                return True
            i+=1
        return False
        