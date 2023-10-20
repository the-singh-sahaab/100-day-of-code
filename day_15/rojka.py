import math
class Solution:
    def isStrictlyPalindromic(self, m: int) -> bool:
        for n in range(1, m+1):
            a = [bin(n)[2:]]
            output = list(map(int, str(a[0])))
            for i in range(len(output)):
                if output[i] == output[i-1]:
                    continue
                else:
                    return False
        return True
        

            


