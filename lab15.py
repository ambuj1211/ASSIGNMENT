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
    
c = int(input("Enter number of columns: "))
r = int(input("Enter number of rows: "))
matrix = [[int(input()) for x in range (c)] for y in range(r)]
DiagCalc(matrix)