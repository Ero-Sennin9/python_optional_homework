import time
import asyncio
from synchronous_calculation import synchronous_calculation
from multi_threading_calculation import multi_threading_calculation
from multi_processing_calculation import multi_processing_calculation
from asynchronous_calculation import asynchronous_calculation
import multiprocessing


def benchmark_calculation(number):
    tasks_number = 1000

    methods = {
        "Синхронный": synchronous_calculation,
        "Многопоточный": multi_threading_calculation,
        "Многопроцессный": multi_processing_calculation,
        "Асинхронный": lambda number_, max_workers_, tasks_number_: asyncio.run(asynchronous_calculation(number_, max_workers_, tasks_number_))
    }

    results = {}
    for name, method in methods.items():
        print("method - ", name)

        start_time = time.time()
        cpu_count = multiprocessing.cpu_count()
        if method is multi_threading_calculation or method is multi_processing_calculation:
            result = method(number, cpu_count)
        elif method is synchronous_calculation:
            result = method(number)
        else:
            result = method(number, cpu_count, tasks_number)

        elapsed = time.time() - start_time
        print("completed")

        results[name] = elapsed
        print(f"{name}: {elapsed:.2f} сек, {len(result)} делителей числа {number}")

    return results
