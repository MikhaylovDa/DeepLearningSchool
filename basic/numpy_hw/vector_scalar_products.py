def scalar_product(v1, v2):
    """  
    <v1, v2> = v1[0] * v2[0] + v1[1] * v2[1] + ... + v1[n] * v2[n]
    
    v1: np.array[, n] --- первая матрица-аргумент длиной n
    v2: np.array[, n] --- вторая матрица-аргумент длиной n
    return product_result: float  --- результат скалярного произведения векторов v1 и v2

    Функция принимает на вход два вектора длиной n
    Возвращает число, равное их скалярному произведению v1 x v2 = product_result 

    Реализуйте скалярное умножение векторов, 
    не используя функции из пакета numpy
    """ 
    product_result = 0
    for elem_v1, elem_v2 in zip(v1, v2):
        product_result += elem_v1 * elem_v2
    return product_result

	
def np_scalar_product(v1, v2):
    """  
    <v1, v2> = v1[0] * v2[0] + v1[1] * v2[1] + ... + v1[n] * v2[n]
    
    v1: np.array[, n] --- первая матрица-аргумент
    v2: np.array[, n] --- вторая матрица-аргумент
    return product_result: float  --- результат скалярного произведения векторов v1 и v2

    Функция принимает на вход два вектора длиной n
    Возвращает число, равное их скалярному произведению v1 x v2 = product_result 

    Реализуйте скалярное умножение векторов, используя функции из пакета numpy
    """ 
    product_result = np.dot(v1, v2)
    return product_result
    

v1 = np.random.sample((1, 3))
v1 = list(a)[0]
v2 = np.random.sample((1, 3))
v2 = list(b)[0]
print(v1, v2)

%time product_1 = scalar_product(v1, v2)
%time product_2 = np_scalar_product(v1, v2)

# проверим корректность:
assert np.allclose(product_1, product_2)