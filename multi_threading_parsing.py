import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from parse_page import parse_page

def multi_threading_parsing(pages_count, max_workers):
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(parse_page, page) for page in range(pages_count)]
        for future in futures:
            results.extend(future.result())
    return results