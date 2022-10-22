import numpy as np


def no_numpy_mult(first, second):
    """
    param first: list of "size" lists, each contains "size" floats
    param second: list of "size" lists, each contains "size" floats
    """
    
    rows_a = len(first)  # Количество строк в первой матрице
    cols_a = len(first[0])  # Количество столбцов в первой матрице
    rows_b = len(second)  # Количество строк во второй матрице
    cols_b = len(second[0])  # Количество столбцов во второй матрице
    
    # Инициализация результирующей матрицы
    result = [[0 for row in range(cols_b)] for col in range(rows_a)]
    
    for row in range(rows_a):
        for col in range(cols_b):
            for col_res in range(cols_a):
                result[row][col] += first[row][col_res] * second[col_res][col]
    return result


def numpy_mult(first, second):
    """
    param first: np.array[size, size]
    param second: np.array[size, size]
    """
    result = np.dot(first, second) 
    return resultu
    
    
first = np.random.sample((100, 100))
second = np.random.sample((100, 100))

M1 = no_numpy_mult(first, second)
M2 = numpy_mult(first, second)

assert np.allclose(np.array(M1), M2)
