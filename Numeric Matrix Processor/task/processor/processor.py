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
4. Horizontal line""")
        choice2 = int(input("Your choice:"))
        n1, m1 = input("Enter matrix size: ").split(" ")
        print("Enter matrix: ")
        matrix1 = Matrix(n1, m1)
        result = matrix1.transpose_matrix(int(choice2))
        result.show_matrix()
