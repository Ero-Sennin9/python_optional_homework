import math
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import freeze_support

from find_factors_in_half_interval import find_factors_in_half_interval

def multi_processing_calculation(number, max_workers):
    result_list = []
    chunk_size = (int(number ** 0.5) + max_workers - 1) // max_workers
    print(max_workers)
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for chunk_ind in range(max_workers):
            futures.append(executor.submit(find_factors_in_half_interval, number, 1 + chunk_ind * chunk_size, 1 + (
                    chunk_ind + 1) * chunk_size))
        for future in futures:
            result = future.result()
            if result is not None:
                result_list += result

    return result_list
