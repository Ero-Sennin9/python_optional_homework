import math

async def find_factors_in_half_interval_async(value, left, right, result_queue):
    if left > right or left < 1:
        raise Exception("Wrong boundaries!!!")
    for i in range(left, right + 1):
        with value.get_lock():
            number = value.value
        rounded_number_sqrt = int(number ** 0.5)
        if i > rounded_number_sqrt:
            break
        if number % i == 0:
            result_queue.put(i)
            if i * i < number:
                result_queue.put(number // i)
