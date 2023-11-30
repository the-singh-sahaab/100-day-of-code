class Solution:
    def grayCode(self, n: int) -> List[int]:
        oldArr = [0,1]
        i = 1
        while i< n:
            Arr = list(oldArr)
            for j in range(len(oldArr)-1,-1,-1):
                Arr.append((2**i)+oldArr[j])
            oldArr = Arr
            i+=1
        return oldArr for i in range(32))