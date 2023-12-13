class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        mat1 = list(zip(*mat))
        res = 0
        for i in range(len(mat)):
            if mat[i].count(1) == 1:
                x = mat[i].index(1)
                if mat1[x].count(1) == 1:
                    res += 1
        return res     