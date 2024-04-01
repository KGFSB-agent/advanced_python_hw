from os import path
import numpy as np

class PrettyMixin:
    def __str__(self):
        return f'Matrix({self.matrix})'

class ExportMixin:
    def export_as_artifact(self, filename):
        with open(path.join("artifacts", "artifacts_3_2", filename), 'w') as f:
            f.write(str(self))

class MatrixBase:
    def __init__(self, matrix: list) -> None:
        
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __add__(self, other: "MatrixBase") -> "MatrixBase":
        if self.rows != other.rows or self.cols != other.cols:
            message = "The matrices must have the same number of rows and columns for addition"
            raise ValueError(message)

        result = []
        for i in range(self.rows):
            result.append([])
            for j in range(self.cols):
                elem = self.matrix[i][j] + other.matrix[i][j]
                result[i].append(elem)

        return type(self)(result)

    def __mul__(self, other: "MatrixBase") -> "MatrixBase":
        if self.rows != other.rows or self.cols != other.cols:
            message = "The matrices must have the same number of rows and columns for addition"
            raise ValueError()

        result = []
        for i in range(self.rows):
            result.append([])
            for j in range(self.cols):
                elem = self.matrix[i][j] * other.matrix[i][j]
                result[i].append(elem)

        return type(self)(result)

    def __matmul__(self, other: "MatrixBase") -> "MatrixBase":
        if self.cols != other.rows:
            message = (
                "The number of columns of the first matrix must match the number of rows"
                " of the second matrix for multiplication"
            )
            raise ValueError(message)

        result = []
        for i in range(self.rows):
            result.append([])
            for j in range(other.cols):
                elem = self.get_matrix_dot_product_elem(self, other, i, j)
                result[i].append(elem)

        return type(self)(result)

    @staticmethod
    def get_matrix_dot_product_elem(matrix1, matrix2, i, j):
        elem_ij = 0
        for k in range(len(matrix1.matrix[i])):
            elem_ij += matrix1.matrix[i][k] * matrix2.matrix[k][j]
        return elem_ij

class SubMixin:
    def __sub__(self, other):
        
        matrix1 = np.array(self.matrix)
        matrix2 = np.array(other.matrix)
        result = matrix1 - matrix2
        result = type(self)(result.tolist())
        return result


class DivMixin:
    def __truediv__(self, other):
        matrix1 = np.array(self.matrix)
        matrix2 = np.array(other.matrix)
        result = matrix1 / matrix2
        result = type(self)(result.tolist())
        return result


class PropertyMixin:
    @property
    def matrix(self):
        
        return self._matrix

    @matrix.setter
    def matrix(self, new_matrix):
        
        self._matrix = new_matrix


class HashMixin:
    def __hash__(self):
        matrix = np.array(self.matrix)
        hash = int(np.sum(matrix) % 10000)
        return hash


class HashMatrix(MatrixBase, HashMixin):
    _hash = set([])
    _hash_prod_result = None

    def __matmul__(self, other: "MatrixBase") -> "MatrixBase":
        hash1, hash2 = hash(self), hash(other)
        if self._hash_prod_result and hash1 in self._hash and hash2 in self._hash:
            result = HashMatrix._hash_prod_result
        else:
            HashMatrix._hash = set([hash1, hash2])
            result = super().__matmul__(other)
            HashMatrix._hash_prod_result = result

        return result

    @staticmethod
    def clear_cache():
        HashMatrix._hash_prod_result = None

class Matrix(
    HashMatrix, HashMixin, PropertyMixin, DivMixin, SubMixin, ExportMixin, PrettyMixin):

    pass

if __name__ == "__main__":
    np.random.seed(0)
    matrix_1_np = np.random.randint(0, 10, (10, 10))
    matrix_1 = matrix_1_np.tolist()
    matrix_1 = Matrix(matrix_1)

    matrix_2_np = np.random.randint(0, 10, (10, 10))
    matrix_2 = matrix_2_np.tolist()
    matrix_2 = Matrix(matrix_2)

    matrix_1.export_as_artifact("artifact_matrix_1.txt")
    matrix_2.export_as_artifact("artifact_matrix_2.txt")

    print("\nПоэлементное сложение матриц:")
    element_wise_sum = matrix_1 + matrix_2
    print(element_wise_sum)
    print("Numpy")
    print(matrix_1_np + matrix_2_np)
    element_wise_sum.export_as_artifact("artifact_element_wise_sum.txt")

    print("\nПоэлементное умножение матриц:")
    element_wise_prod = matrix_1 * matrix_2
    print(element_wise_prod)
    print("Numpy")
    print(matrix_1_np * matrix_2_np)
    element_wise_prod.export_as_artifact("artifact_element_wise_prod.txt")

    print("\nУмножение матриц:")
    matrix_prod = matrix_1 @ matrix_2
    print(matrix_prod)
    print("Numpy")
    print(matrix_1_np @ matrix_2_np)
    matrix_prod.export_as_artifact("artifact_matrix_prod.txt")