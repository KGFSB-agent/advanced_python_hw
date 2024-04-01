import numpy as np
from os import path

class Matrix:
    def __init__(self, data):
        self.data = data
        self.nrows = len(data)
        self.ncols = len(data[0])

    def __add__(self, other):
        if self.nrows != other.nrows or self.ncols != other.ncols:
            raise ValueError("Matrices must have the same dimensions")
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(self.ncols)] for i in range(self.nrows)])

    def __mul__(self, other):
        if self.nrows != other.nrows or self.ncols != other.ncols:
            raise ValueError("Matrices must have the same dimensions")
        return Matrix([[self.data[i][j] * other.data[i][j] for j in range(self.ncols)] for i in range(self.nrows)])

    def __matmul__(self, other):
        if self.ncols != other.nrows:
            raise ValueError("Matrices must have the same inner dimensions")
        return Matrix([
            [sum(self.data[i][k] * other.data[k][j] for k in range(self.ncols)) for j in range(other.ncols)]
            for i in range(self.nrows)
        ])

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])

def create_artifact(matrix, filename):
    with open(path.join("artifacts", "artifacts_3_1", filename), 'w') as f:
        f.write(str(matrix))

if __name__ == "__main__":
    np.random.seed(0)

    m1 = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
    m2 = Matrix(np.random.randint(0, 10, (10, 10)).tolist())

    m_add = m1 + m2
    m_mul = m1 * m2
    m_matmul = m1 @ m2

    # Windows не разрешает мне назвать файл со "*"
    create_artifact(m_add, 'matrix_add.txt')
    create_artifact(m_mul, 'matrix_mul.txt')
    create_artifact(m_matmul, 'matrix_matmul.txt')

