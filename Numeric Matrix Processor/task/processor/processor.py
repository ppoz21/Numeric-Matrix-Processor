class Matrix:
    """Class for matrix"""
    def __init__(self, n, m):
        self.rows = int(n)
        self.columns = int(m)
        self.matrix = []
        self.read_matrix()

    def read_matrix(self):
        for i in range(self.rows):
            row = input().split()
            self.matrix.append([])
            for j in range(self.columns):
                self.matrix[i].append(float(row[j]))

    def add_matrices(self, matrix):
        n = self.rows
        m = self.columns
        elements = []
        for i in range(self.rows):
            for j in range(self.columns):
                elements.append(self.matrix[i][j] + matrix.matrix[i][j])
        return CreatedMatrix(n, m, *elements)

    def multiplication_by_number(self, number):
        n = self.rows
        m = self.columns
        elements = []
        for i in range(self.rows):
            for j in range(self.columns):
                elements.append(self.matrix[i][j] * number)
        return CreatedMatrix(n, m, *elements)

    def multiplication_by_matrix(self, matrix):
        n1 = self.rows
        m1 = self.columns
        n2 = matrix.rows
        m2 = matrix.columns
        elements = []
        for i in range(n1):
            for j in range(m2):
                dot_product = 0
                for k in range(m1):
                    multiplication = self.matrix[i][k] * matrix.matrix[k][j]
                    dot_product += multiplication
                elements.append(dot_product)
        return CreatedMatrix(n1, m2, *elements)

    def transpose_matrix(self, transposition):
        if transposition == 1:
            return self.transpose_main_diagonal()
        elif transposition == 2:
            return self.transpose_side_diagonal()
        elif transposition == 3:
            return self.transpose_vertical_line()
        elif transposition == 4:
            return self.transpose_horizontal_line()
        else:
            raise Exception("Operation cannot be performed.")

    def transpose_main_diagonal(self):
        n = self.rows
        m = self.columns
        elements = []
        for i in range(n):
            for j in range(m):
                elements.append(self.matrix[j][i])

        return CreatedMatrix(n, m, *elements)

    def transpose_side_diagonal(self):
        n = self.rows
        m = self.columns
        elements = []
        rows = list(range(n))
        rows.reverse()
        col = list(range(m))
        col.reverse()

        for i in rows:
            for j in col:
                elements.append(self.matrix[j][i])

        return CreatedMatrix(n, m, *elements)

    def transpose_vertical_line(self):
        n = self.rows
        m = self.columns
        elements = []

        col = list(range(m))
        col.reverse()

        for i in range(n):
            for j in col:
                elements.append(self.matrix[i][j])
        return CreatedMatrix(n, m, *elements)

    def transpose_horizontal_line(self):
        n = self.rows
        m = self.columns
        elements = []

        row = list(range(n))
        row.reverse()
        for i in row:
            for j in range(m):
                elements.append(self.matrix[i][j])

        return CreatedMatrix(n, m, *elements)

    def determinant_of_matrix(self):
        n = self.rows
        mat = self.matrix
        temp = [0] * n  # temporary array for storing row
        total = 1
        det = 1  # initialize result

        # loop for traversing the diagonal elements
        for i in range(0, n):
            index = i  # initialize the index

            # finding the index which has non zero value
            while mat[index][i] == 0 and index < n:
                index += 1

            if index == n:  # if there is non zero element
                # the determinat of matrix as zero
                continue

            if index != i:
                # loop for swaping the diagonal element row and index row
                for j in range(0, n):
                    mat[index][j], mat[i][j] = mat[i][j], mat[index][j]

                    # determinant sign changes when we shift rows
                # go through determinant properties
                det = det * int(pow(-1, index - i))

                # storing the values of diagonal row elements
            for j in range(0, n):
                temp[j] = mat[i][j]

                # traversing every row below the diagonal element
            for j in range(i + 1, n):
                num1 = temp[i]  # value of diagonal element
                num2 = mat[j][i]  # value of next row element

                # traversing every column of row
                # and multiplying to every row
                for k in range(0, n):
                    # multiplying to make the diagonal
                    # element and next row element equal

                    mat[j][k] = (num1 * mat[j][k]) - (num2 * temp[k])

                total = total * num1  # Det(kA)=kDet(A);

        # mulitplying the diagonal elements to get determinant
        for i in range(0, n):
            det = det * mat[i][i]
        return float(det / total)  # Det(kA)/k=Det(A);

    def show_matrix(self):
        for row in range(self.rows):
            for column in range(self.columns):
                print(self.matrix[row][column], end=" ")
            print("")
        print()


class CreatedMatrix(Matrix):
    def __init__(self, n, m, *elements):
        self.rows = int(n)
        self.columns = int(m)
        self.matrix = []
        self.create_matrix(elements)

    def create_matrix(self, elements):
        k = 0
        for i in range(self.rows):
            self.matrix.append([])
            for j in range(self.columns):
                self.matrix[i].append(elements[k])
                k += 1


while True:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
0. Exit""")
    choice = int(input("Your choice: "))
    if choice == 0:
        break
    elif choice == 1:
        n1, m1 = input("Enter size of first matrix: ").split(" ")
        print("Enter first matrix: ")
        matrix1 = Matrix(n1, m1)
        n2, m2 = input("Enter size of second matrix: ").split(" ")
        print("Enter second matrix: ")
        matrix2 = Matrix(n2, m2)
        if n1 == n2 and m1 == m2:
            result = matrix1.add_matrices(matrix2)
            print("The result is:")
            result.show_matrix()
        else:
            print("The operation cannot be performed.")
    elif choice == 2:
        n1, m1 = input("Enter size of matrix: ").split(" ")
        print("Enter matrix: ")
        matrix1 = Matrix(n1, m1)
        c = float(input("Enter constant: "))
        print("The result is: ")
        result = matrix1.multiplication_by_number(c)
        result.show_matrix()
    elif choice == 3:
        n1, m1 = input("Enter size of first matrix: ").split(" ")
        print("Enter first matrix: ")
        matrix1 = Matrix(n1, m1)
        n2, m2 = input("Enter size of second matrix: ").split(" ")
        print("Enter second matrix: ")
        matrix2 = Matrix(n2, m2)
        if m1 == n2:
            result = matrix1.multiplication_by_matrix(matrix2)
            print("The result is: ")
            result.show_matrix()
        else:
            print("The operation cannot be performed.")
    elif choice == 4:
        print("""
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
""")
        choice2 = int(input("Your choice:"))
        n1, m1 = input("Enter matrix size: ").split(" ")
        print("Enter matrix: ")
        matrix1 = Matrix(n1, m1)
        result = matrix1.transpose_matrix(int(choice2))
        result.show_matrix()
    elif choice == 5:
        n1, m1 = input("Enter size of matrix: ").split(" ")
        print("Enter matrix: ")
        matrix1 = Matrix(n1, m1)
        if n1 == m1:
            print("The result is: ")
            determ = matrix1.determinant_of_matrix()
            print(determ)
