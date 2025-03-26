import numpy as np
from matrix import Matrix

def run_simple_operations():
    matrix1 = np.random.randint(0, 10, (10, 10)).tolist()
    matrix2 = np.random.randint(0, 10, (10, 10)).tolist()
    m1 = Matrix(matrix1)
    m2 = Matrix(matrix2)
    result_add = m1 + m2
    result_mul = m1 * m2
    result_matmul = m1 @ m2
    with open('artifacts/task_1/matrix1.txt', 'w') as f:
        f.write(str(m1))
    with open('artifacts/task_1/matrix2.txt', 'w') as f:
        f.write(str(m2))
    with open('artifacts/task_1/matrix+.txt', 'w') as f:
        f.write(str(result_add))
    with open('artifacts/task_1/matrix*.txt', 'w') as f:
        f.write(str(result_mul))
    with open('artifacts/task_1/matrix@.txt', 'w') as f:
        f.write(str(result_matmul))
if __name__ == '__main__':
    run_simple_operations()