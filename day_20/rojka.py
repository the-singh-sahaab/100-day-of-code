import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        mat = np.asarray(mat)
        try:
            return mat.reshape(r,c)
        except ValueError:
            return mat
        