import numpy as np
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n=len(grid), len(grid[0])
        grid=np.asarray(grid)
        cols=np.sum(grid, axis=0)
        rows=np.sum(grid, axis=1)
        rows=rows.reshape(m, 1)      
        grid=2*(rows+cols)-(m+n)
        return grid

        # did this but facing tle
        # grid1 = np.transpose(grid)
        # print(np.array(grid))
        # new1 = []
        # for i in grid:
        #     new = []
        #     for j in grid1:
        #         new.append(((sum(j))+sum(i))-((len(j)-sum(j))+(len(i)-sum(i))))
        #     new1.append(new)
        # return new1
