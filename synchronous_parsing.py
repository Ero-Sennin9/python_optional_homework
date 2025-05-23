import requests
from bs4 import BeautifulSoup
from parse_page import parse_page

def synchronous_parsing(pages_count):
    results = []
    for page in range(pages_count):
        results += parse_page(page)
    return results