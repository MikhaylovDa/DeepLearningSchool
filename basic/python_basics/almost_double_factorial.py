def almost_double_factorial(n):
    count = 1
    fact = 1
    while count <= n:
        if count % 2 == 0:
            count += 1
        else:
            fact *= count
            count += 1
    return fact

