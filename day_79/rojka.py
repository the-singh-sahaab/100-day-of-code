class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        k = 0
        while k < 4:
            for i in range(len(mat)):
                for j in range(i):
                    mat[i][j],mat[j][i] = mat[j][i],mat[i][j]

            n = len(mat)
            for i in range(n):
                for j in range(n // 2):
                    mat[i][j], mat[i][-j - 1] = mat[i][-j - 1], mat[i][j]
            if mat==target:
                return mat==target
            k+=1
        return False