matrix=[[2,4,5,1], [3,2,9,6] , [1,0,2,10] ]
for i in range(len(matrix)):
 matrix[i]=sum(matrix[i])


print(matrix)
print(matrix.index(max(matrix)))