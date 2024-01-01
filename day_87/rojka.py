class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        i, j, ans = 0, 0, 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                ans += 1
                i += 1
            j += 1

        return ans
        