class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = len(s)
        count = 0
        for i in range(l):
            if s[i] in {'a','e','i','o','u','A','E','I','O','U'}:
                if i<l//2:
                    count+=1
                else:
                    count-=1
        return count==0