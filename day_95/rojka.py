class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        rowj,colj,p,c,d,mat=0,0,n*n,1,1,[[0 for i in range(n)] for i in range(n)]
        while p>c-1:
            mat[rowj][colj]=c
            if d==1:
                if   colj+1<n   and  mat[rowj][colj+1]==0 : 
                    colj , d = colj+1 , 1
                elif rowj+1<n   and  mat[rowj+1][colj]==0 :
                    rowj , d = rowj+1 , 2
            elif d==2:
                if   rowj+1<n   and  mat[rowj+1][colj]==0 :
                    rowj , d = rowj+1 , 2
                elif colj-1>=0  and  mat[rowj][colj-1]==0 :
                    colj , d = colj-1 , 3
            elif d==3:
                if   colj-1>=0  and  mat[rowj][colj-1]==0 :
                    colj , d = colj-1 , 3
                elif rowj-1>=0  and  mat[rowj-1][colj]==0 :
                    rowj , d = rowj-1 , 4
            elif d==4:
                if   rowj-1>=0  and  mat[rowj-1][colj]==0 :
                    rowj , d = rowj-1 , 4
                elif colj+1<n   and  mat[rowj][colj+1]==0 :
                    colj , d = colj+1 , 1
            c+=1
        return mat
# new_matrix = np.zeros((n, n))
# print(new_matrix)
# i = 0
# j = 0
# for a in range(1,(n**2)+1):
#     if i >= 0 and j == 0 and i<n:
#         if i < n and j < n and new_matrix[j][i]==0:
#             new_matrix[j][i] =a
#             i += 1
#         print(new_matrix)
            
#     elif i >= 1 and j <= n :
#         if i < n and j < n and new_matrix[j-1][i-1]==0:
#             new_matrix[j-1][i-1] = a
#             j -= 1
#         else:
#             new_matrix[i][j]=a
#             i += 1  
#         print(new_matrix)
            
#     elif i <= n and j == n-1 :
#         if i <= n and j < n and new_matrix[j][i-2]==0:
#             i -= 1
#             new_matrix[j][i-1] = a
#         print(new_matrix)
            
#     elif i == n and j >= 0 and  j < n -1:
#         if i <= n and j < n and new_matrix[j+1][i-1]==0:
#             new_matrix[j+1][i-1] = a
#             j += 1
    
#         print(new_matrix)