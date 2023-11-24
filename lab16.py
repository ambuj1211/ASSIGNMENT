def snake(matrix):
    result = []
    for i, row in enumerate(matrix):
        if i % 2 == 0:
            result.extend(row)
        else:
            result.extend(row[::-1])
    return result

c = int(input("Enter number of columns: "))
r = int(input("Enter number of rows: "))
matrix = [[int(input()) for x in range (c)] for y in range(r)]

output = snake(matrix)
print(output)