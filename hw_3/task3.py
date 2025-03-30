import numpy as np
from matrix import Matrix
from matrix import HashMixin
import random

def find_collision():
    while True:
        rows = random.randint(1, 10)
        cols = random.randint(1, 10)
        A = Matrix(np.random.randint(0, 100, (rows, cols)).tolist())
        C = Matrix(np.random.randint(0, 100, (rows, cols)).tolist())
        if not (hash(A) == hash(C) and A != C):
            continue
        b_rows = cols
        b_cols = rows
        B = Matrix(np.random.randint(0, 100, (b_rows, b_cols)).tolist())
        D = B
        AB = A @ B
        CD = C @ D
        if A @ B == C @ D:
            continue
        save_matrix(A, 'A.txt')
        save_matrix(B, 'B.txt')
        save_matrix(C, 'C.txt')
        save_matrix(D, 'D.txt')
        save_matrix(AB, 'AB.txt')
        save_matrix(CD, 'CD.txt')
        with open('artifacts/task_3/hash.txt', 'w') as f:
            f.write(f"Hash of AB: {hash(AB)}\nHash of CD: {hash(CD)}")
        break

def save_matrix(matrix, filename):
    with open(f'artifacts/task_3/{filename}', 'w') as f:
        f.write(str(matrix))

if __name__ == '__main__':
    find_collision()