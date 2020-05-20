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
                self.matrix[i].append(int(row[j]))

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

    def show_matrix(self):
        for row in range(self.rows):
            for column in range(self.columns):
                print(self.matrix[row][column], sep=" ", end=" ")
            print("\n")


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


n1, m1 = input().split(" ")
matrix1 = Matrix(n1, m1)
c = int(input())
new_matrix = matrix1.multiplication_by_number(c)
new_matrix.show_matrix()
