import numpy as np


def np_diag_2k(given_matrix):
    """  
    given_matrix: np.array[m, m] --- первая матрица-аргумент
    return c: float   --- сумма элементов массива given_matrix, принадлежащих диагонали и являющимися четными

    Функция принимает на вход квадратную матрицу размерностью m x m и возвращает число,
    равное сумме четных диагональных элементов этой квадратной матрицы

    """ 
    # Получаем массив из элементов главной диагонали матрицы
    matrix_main_diagonal = np.diagonal(given_matrix, offset=0)
    sum_even_elements = 0
    sum_even_elements = np.sum(matrix_main_diagonal[matrix_main_diagonal % 2 == 0])
    return sum_even_elements

 
# зададим некоторую квадратную матрицу
a = np.random.randint(1, 10, size=(5, 5))

%%time
# засечем время работы функции с NumPy
print(np_diag_2k(a))