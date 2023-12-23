class Solution:
    def maxScore(self, s: str) -> int:
        max = -1
        for i in range(1,len(s)):
            left = s[:i]
            right = s[i:]
            if max < left.count("0") + right.count("1"):
                max = left.count("0") + right.count("1")
        return max

