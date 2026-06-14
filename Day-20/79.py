#write a program to find row - wise sum.
def row_wise_sum(matrix):
    row_sums = []
    for row in matrix:
        row_sums.append(sum(row))
    return row_sums
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sums = row_wise_sum(matrix)
print("Row-wise sums:", sums)





                    