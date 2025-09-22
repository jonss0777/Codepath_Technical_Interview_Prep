
'''
Problem 1: Transpose Matrix

Write a function transpose() that accepts a 2D integer array 
matrix and returns the transpose of matrix. The transpose of 
a matrix is the matrix flipped over its main diagonal,
swapping the rows and columns.


U: 

Swap elements along the diagnonal 

Note: we will only look through half of the matrix 

O(n^2/2) => O(n^2)

P:

for i in n :
    for j in i+1:
        swap ( (i,j), (j,i))

[1,2]
[4,3]

I:

'''

def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    # square matrix
    if n == m:
        for i in range(n) :
            for j in range(i+1):
                matrix[i][j] , matrix[j][i]=  matrix[i][j], matrix[j][i]
        return matrix 
    else:
        transpose = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(matrix[j][i])
            transpose.append(row)
        return transpose
    

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(matrix))


