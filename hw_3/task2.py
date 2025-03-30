import numpy as np

from mixins import ArrayWithFeatures

if __name__ == "__main__":
    matrix1 = ArrayWithFeatures(np.random.randint(0, 10, (10, 10)))
    matrix2 = ArrayWithFeatures(np.random.randint(0, 10, (10, 10)))
    matrix1.save('artifacts/task_2/matrix1.txt')
    matrix2.save('artifacts/task_2/matrix2.txt')
    result_add = matrix1 + matrix2
    result_mul = matrix1 * matrix2
    result_matmul = matrix1 @ matrix2
    result_add.save('artifacts/task_2/matrix+.txt')
    result_mul.save('artifacts/task_2/matrix*.txt')
    result_matmul.save('artifacts/task_2/matrix@.txt')

