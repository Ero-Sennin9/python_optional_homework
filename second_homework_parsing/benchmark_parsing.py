import time
import asyncio
from synchronous_parsing import synchronous_parsing
from multi_threading_parsing import multi_threading_parsing
from multi_processing_parsing import multi_processing_parsing
from asynchronous_parsing import async_parsing
import multiprocessing


def benchmark_parsing(pages_count):
    methods = {
        "Синхронный": synchronous_parsing,
        "Многопоточный": multi_threading_parsing,
        "Многопроцессный": multi_processing_parsing,
        "Асинхронный": lambda pages_count_: asyncio.run(async_parsing(pages_count_))
    }

    results = {}
    for name, method in methods.items():
        print("method - ", name)

        start_time = time.time()

        if not (method is multi_threading_parsing or method is multi_processing_parsing):
            result = method(pages_count)
        else:
            cpu_count = min(multiprocessing.cpu_count(), pages_count)
            result = method(pages_count, cpu_count)
        elapsed = time.time() - start_time

        print("completed")

        results[name] = elapsed
        print(f"{name}: {elapsed:.2f} сек, {len(result)} статей")

    return results
