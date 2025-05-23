import math

def find_factors_in_half_interval(number, left, right):
    result_list = []
    if left > right or left < 1:
        raise Exception("Wrong boundaries!!!")
    for i in range(left, right + 1):
        if number % i == 0:
            result_list.append(i)
            if i * i < number:
                result_list.append(number // i)
    return result_list

