class Solution:
    def longestValidParentheses(self, s: str) -> int:
        new = []
        for i in s:
            inner = []
            if i == "(":
                inner.append(i)
                new.append(inner)
            else:
                if new is not None:
                    a = 0
                    for j in new[::-1]:
                        if len(j) == 1:
                            j.append(i)
                            a +=1
                            break
                    if a == 0:
                        new.append([])
        # print(new.count(["(",")"])*2)
        m = []
        n = 0
        for i in new:
            if len(i) == 2:
                n += 1
            else:
                m.append(n)
                n = 0
        m.append(n)
        return max(m)*2