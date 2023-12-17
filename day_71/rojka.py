class Solution:
    def divideArray(self, num: List[int], k: int) -> List[List[int]]:
        num.sort()
        new = []
        for i in range(0,len(num),3):
            a, b, c = num[i:i+3]

            if c - a <= k:
                new.append([a, b, c])
            else:
                new.clear()
                return new
        return new
        