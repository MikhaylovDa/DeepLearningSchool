def cumsum_and_erase(array_a, erase=1):
    result_array = []
    elem_arr_sum = 0
    for i in range(len(array_a)):
        elem_arr_sum += array_a[i]
        if elem_arr_sum != erase:
            result_array.append(elem_arr_sum)
    return result_array
