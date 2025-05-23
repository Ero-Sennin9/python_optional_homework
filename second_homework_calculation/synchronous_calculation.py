from find_divisors_in_half_interval import find_divisors_in_half_interval

def synchronous_calculation(number):
    return find_divisors_in_half_interval(number, 1, int(number ** 0.5) + 1)
