def PrintMatrix(Matrix):
    for row_index, row in enumerate(Matrix[1:]):
        for element_index, element in enumerate(row):
            print("{}  ".format(' ' * (Matrix[0][element_index] - len(element)) + element), end="")
        if row_index < len(Matrix) - 2:
            print("")


def Matrix_Input(m, n):
    matrix = [[0] * n]
    print(
        "Enter the values row by row. Separate each value with a comma. If the value is 0, you can use a space instead of entering 0. Do not use spaces anywhere else.")
    for i in range(m):
        output_string = "Enter the values in row " + str(i + 1) + ": "
        row = input(output_string)
        if row.count(",") >= n:
            print("Error: entered more values than asked for")
            return 0
        matrix_row = row.split(",")
        for index_x, x in enumerate(matrix_row):
            if x != " ":
                matrix_row[index_x] = x
                if matrix[0][index_x] < len(x):
                    matrix[0][index_x] = len(x)
            else:
                matrix_row[index_x] = '0'
        matrix.append(matrix_row)

    return matrix


def getColumns(Matrix):
    return_Matrix = [[x] for x in Matrix[1]]
    for row in Matrix[2:]:
        for element_index, element in enumerate(row):
            return_Matrix[element_index].append(element)
    return return_Matrix


def RowColumnProdSum(row, column):
    sumTotal = 0
    i = 0
    while i < len(row):
        sumTotal += int(row[i]) * int(column[i])
        i += 1
    return str(sumTotal)


def Matrix_Multiplication():
    print("Enter the two matrices you want to multiply")
    print("Matrix A: ")
    print("---------")
    matrixA_rows = int(input("Number of rows in your matrix: "))
    matrixA_columns = int(input("Number of columns in your matrix: "))
    matrixA = Matrix_Input(matrixA_rows, matrixA_columns)
    print("\nThis is your matrix A:\n")
    PrintMatrix(matrixA)
    print("")
    print("\nMatrix B: ")
    print("---------")
    matrixB_rows = int(input("Number of rows in your matrix: "))
    matrixB_columns = int(input("Number of columns in your matrix: "))
    matrixB = Matrix_Input(matrixB_rows, matrixB_columns)
    print("\nThis is your matrix B:\n")
    PrintMatrix(matrixB)
    print("")
    if matrixA_columns != matrixB_rows:
        print("\nThe matrices entered can't be multiplied. Please enter a valid input")
        again_or_not = input("Do you want to enter the matrices again? (y/n): ")
        if again_or_not == "y":
            Matrix_Multiplication()
            return 0
        else:
            return -1
    else:
        prod_matrix = [[0] * matrixB_columns]
        for row in matrixA[1:]:
            row_prod = []
            for index_column, column in enumerate(getColumns(matrixB)):
                prod_rc = RowColumnProdSum(row, column)
                row_prod.append(prod_rc)
                prod_matrix[0][index_column] = max(prod_matrix[0][index_column], len(prod_rc))
            prod_matrix.append(row_prod)
        print("\nResult:\n")
        print("-------")
        PrintMatrix(prod_matrix)
        print("")


Matrix_Multiplication()
