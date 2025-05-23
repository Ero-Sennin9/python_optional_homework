from concurrent.futures import ThreadPoolExecutor
from find_divisors_in_half_interval import find_divisors_in_half_interval


def multi_threading_calculation(number, max_workers):
    chunk_size = (int(number ** 0.5) + max_workers - 1) // max_workers
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for chunk_ind in range(max_workers):
            futures.append(executor.submit(find_divisors_in_half_interval, number, 1 + chunk_ind * chunk_size, 1 + (
                chunk_ind + 1) * chunk_size))
        for future in futures:
            results += future.result()
    return results
