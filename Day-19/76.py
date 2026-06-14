#write a program to find diagonal sum.
def diagonal_sum(matrix):
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    n = len(matrix)
    
    for i in range(n):
        primary_diagonal_sum += matrix[i][i]
        secondary_diagonal_sum += matrix[i][n - 1 - i]
    
    return primary_diagonal_sum, secondary_diagonal_sum
# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
primary_sum, secondary_sum = diagonal_sum(matrix)

print("Primary diagonal sum:", primary_sum)
print("Secondary diagonal sum:", secondary_sum)







                                