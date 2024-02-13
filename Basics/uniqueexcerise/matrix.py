m = [[1,2,3], [4,5,6]]

ROW = int(input("Enter number of rows: "))
COLUMNS = int(input("Enter number of columns: "))

matrix = []
print("Enter the values in row: ")

for i in range(ROW):
    a = []
    for j in range(COLUMNS):
        a.append(int(input("Enter the values in column: ")))
    matrix.append(a)
    
# TODO: print the matrix3

for i in range(ROW):
    for j in range(COLUMNS):
        print(matrix[i],[j], end=" ")
    print()