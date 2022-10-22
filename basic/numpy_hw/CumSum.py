import numpy as np


def cumsum(A):
    """  
    A: np.array[num_row, num_column]        --- матрица-аргумент
    return S: np.array[num_row, num_column] --- выходная матрица кумулятивных сумм

    Функция принимает на вход матрицу A размерностью n x m и возвращает 
    матрицу с той же размерностью n x m, i-ая строчка которой есть последовательность 
    кумулятивных сумм элементов i-ой строки матрицы A

    В реализации этой функции необходимо использовать функционал пакета numpy
    """ 
    
    if A.ndim == 1:  # A - vector
        return np.cumsum(A)
    else:
        result = np.zeros(shape=A.shape)
        for count in range(A.shape[0]):
            result[count] = np.cumsum(A[count])
        return result
        

data_for_test_1 = np.array([1, 2, 3, 4, 5])
data_for_test_2 = np.array([[7, 15, 40], [200, 70, 60], [45, 38, 72]])

# if data for test is vector
assert np.allclose(cumsum(data_for_test_1), np.cumsum(data_for_test_1))

# if data for test is 2-dim array
assert np.allclose(cumsum(data_for_test_2), np.cumsum((data_for_test_2))

