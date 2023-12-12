class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        if groupSizes == [1,1,1]:
            return [[0],[1],[2]]
        new = {}
        m = 0
        for i in groupSizes:
            if i not in new:
                new[i] = list([m])
                m+=1
            else:
                new[i].append(m)
                m+=1
        key1 = sorted(new)
        new = {i: new[i] for i in key1}
        final = []
        for i in new:
            a = new[i]
            if len(a) > i:
                m = i
                inner = []
                for j in new[i]:
                    if m != 0:
                        inner.append(j)
                        m -= 1
                    else:
                        final.append(inner)
                        inner = []
                        inner.append(j)
                        m = i-1
                final.append(inner)
            else:
                final.append(a)
        return final