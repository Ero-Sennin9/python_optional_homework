import asyncio
from concurrent.futures import ProcessPoolExecutor

from find_divisors_in_half_interval import find_divisors_in_half_interval
async def asynchronous_calculation(number, max_workers, tasks_count):
    loop = asyncio.get_running_loop()

    chunk_size = (int(number ** 0.5) + tasks_count - 1) // tasks_count
    tasks = []

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        for chunk_ind in range(tasks_count):
            tasks.append(loop.run_in_executor(executor, find_divisors_in_half_interval, number, 1 + chunk_ind * chunk_size, 1 + (chunk_ind + 1) * chunk_size))

    tasks_results = await asyncio.gather(*tasks)
    results = []
    for find_divisors_results in tasks_results:
        results.extend(find_divisors_results)
    return results