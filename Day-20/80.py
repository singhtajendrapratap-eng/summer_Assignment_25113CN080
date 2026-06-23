#write a program to find column wise sum.
def column_wise_sum(matrix):
    if not matrix:
        return []
    
    num_columns = len(matrix[0])
    column_sums = [0] * num_columns
    
    for row in matrix:
        for i in range(num_columns):
            column_sums[i] += row[i]
    
    return column_sums
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sums = column_wise_sum(matrix)
print("Column-wise sums:", sums)

