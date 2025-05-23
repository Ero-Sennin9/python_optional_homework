def find_divisors_in_half_interval(number, left, right):
    if left > right or left < 1:
        raise Exception("Wrong boundaries!!!")

    divisors = []
    for i in range(left, right + 1):
        if number % i == 0:
            divisors.append(i)
            if number // i != i:
                divisors.append(number // i)
    return divisors