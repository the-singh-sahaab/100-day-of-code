class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        new = []
        for i in bank:
            if "1" in i:
                new.append(i.count("1"))
        sum1 = 0
        for i in range(len(new)-1):
            sum1 += (new[i]*new[i+1])
        return sum1

        