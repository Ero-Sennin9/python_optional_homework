import math
from multiprocessing import Value, Queue
from find_factors_in_half_interval_with_heuristic import find_factors_in_half_interval

def synchronous_calculation(number):
    value = Value('i', number, lock=True)
    queue = Queue()
    find_factors_in_half_interval(value, 1, int(number * 0.5) + 1, queue)
    result = []
    while not queue.empty():
        result.append(queue.get())
    return result
