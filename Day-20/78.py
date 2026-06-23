#write a program to check symmetric matrix.
def is_symmetric_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    if rows != cols:
        return False
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    
    return True
matrix1 = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
matrix2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print("Matrix 1 is symmetric:", is_symmetric_matrix(matrix1))
print("Matrix 2 is symmetric:", is_symmetric_matrix(matrix2))


