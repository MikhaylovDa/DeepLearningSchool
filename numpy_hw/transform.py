import numpy as np
from copy import copy


def transform(X, a=1):
    """  
    X: np.array[num_row, num_column]          --- матрица-аргумент
    a: float                                  --- значение для преобразования нечетных элементов строк в X
    return S: np.array[num_row, num_column*2] --- матрица, где строки являются 
    сконкатенированными строками изначальной матрицы X со строками, являющимися их преобразованиями

    Функция принимает на вход матрицу X размерностью n x m, число a и 
    возвращает  матрицу с размерностью n x m*2, i-ая строчка которой является склеенной
    i-ой строкой X с ее преобразованием ее строки transformation(X[i]), записанном в обратном порядке, 
    где преобразование для числа k определено как:
    transformation(k) = a if ind(k) % 2 == 0 else k**3

    В реализации этой функции необходимо использовать функционал пакета numpy

    """ 
    result = X.copy()
    result[:, ::2] = result[:,::2]**3
    result[:, 1::2] = a  
    result[:,:] = result[:,::-1]
    return np.concatenate([X.copy(), result], axis=1)
    
