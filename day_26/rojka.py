class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        new = []
        for i in range(len(pref)):
            if i == 0:
                new.append(pref[i])
            else:
                new.append(pref[i-1]^pref[i])
        return new
