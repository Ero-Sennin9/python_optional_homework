from concurrent.futures import ProcessPoolExecutor
from parse_page import parse_page

def multi_processing_parsing(pages_count, max_workers):
    results = []
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(parse_page, page) for page in range(pages_count)]
        for future in futures:
            results.extend(future.result())
    return results