def DiagCalc(matrix):
    if not all(len(row) == len(matrix) for row in matrix):
        print("Input matrix is not square.")
        return
    
left_diag_sum = 0
right_diag_sum = 0

for i in range(len(matrix)):
    left_diag_sum += matrix[i][i] 
    right_diag_sum += matrix[i][len(matrix) - 1 - i] 

print("Sum of left diagonal:", left_diag_sum)
print("Sum of right diagonal:", right_diag_sum)

matrix = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
DiagCalc(matrix)