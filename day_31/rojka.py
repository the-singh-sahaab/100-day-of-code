class Solution:
    def combinationSum(self, candidates: List[int], traget: int) -> List[List[int]]:
        ans  = []
        ds = []
        def Findcombinations(inti_num: int, traget: int):
            if inti_num == len(candidates):
                if traget == 0:
                    ans.append(ds[:])
                return 
            if candidates[inti_num]<=traget:
                ds.append(candidates[inti_num])
                Findcombinations(inti_num, traget - candidates[inti_num])
                ds.pop()
            Findcombinations(inti_num+1,traget)
        Findcombinations(0, traget)
        return ans