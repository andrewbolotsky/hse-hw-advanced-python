import typing

TMatrix = typing.TypeVar("TMatrix", bound="Matrix")


class Matrix:

    def __init__(self, matrix: list[list[int]]):
        self._matrix = matrix
        self._rows = len(matrix)
        if self._rows == 0:
            self._columns = 0
        else:
            self._columns = len(matrix[0])

    def __add__(self, other: TMatrix) -> TMatrix:
        self._check_same_dimensions(other)
        matrix_list = [[other._matrix[i][j] + self._matrix[i][j] for j in range(self._columns)] for i in range(self._rows)]
        return Matrix(matrix_list)

    def __mul__(self, other: TMatrix) -> TMatrix:
        self._check_same_dimensions(other)
        matrix_list = [[other._matrix[i][j] * self._matrix[i][j] for j in range(self._columns)] for i in
                       range(self._rows)]
        return Matrix(matrix_list)

    def __str__(self) -> str:
        result = "["
        for i in range(self._rows):
            if i == self._rows - 1:
                result += f"{self._matrix[i]}"
            else:
                result += f"{self._matrix[i]},\n"
        return result + "]"
    def __matmul__(self, other: TMatrix) -> TMatrix:
        self._check_transpon_dimensions(other)
        matrix_list = []
        for i in range(len(self._matrix)):
            row = []
            for j in range(other._columns):
                sum_product = 0
                for k in range(len(other._matrix)):
                    sum_product += self._matrix[i][k] * other._matrix[k][j]
                row.append(sum_product)
            matrix_list.append(row)
        return Matrix(matrix_list)

    def _check_same_dimensions(self, other: TMatrix):
        if other._rows != self._rows or other._columns != self._columns:
            raise ValueError("Matrix cannot be added with different sizes.")

    def _check_transpon_dimensions(self, other: TMatrix):
        if other._rows != self._columns or other._columns != self._rows:
            raise ValueError("Matrix cannot be added with different sizes.")