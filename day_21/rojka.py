class Solution:
    def removeStars(self, s: str) -> str:
        new_stack = []
        for i in range(len(s)):
            if s[i] == "*":
                new_stack.pop()
                continue
            else:
                new_stack.append(s[i])
        lsit1 = ""
        for j in new_stack:
            lsit1 += j
        return lsit1 


