class Solution:
    def combinationSum2(self, candidates: List[int], traget: int) -> List[List[int]]:
        final = []
        an = []
        candidates.sort()
        def recur(index_val:int, traget:int):
            if traget == 0:
                final.append(an[:])
                return 
            for i in range(index_val, len(candidates)):
                if i > index_val and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > traget:
                    break
                an.append(candidates[i])
                recur(i+1, traget - candidates[i])
                an.pop()
        recur(0, traget)
        return final
