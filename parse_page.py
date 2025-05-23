import requests
from bs4 import BeautifulSoup

def parse_page(page):
    url = f"https://nauchforum.ru/archive/article/all?page={page}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    while response.status_code != 200:
        response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []
    for li in soup.select('ul.archive-list li'):
        title = li.find('a').text.strip()
        authors = li.find('strong', text='Авторы:').next_sibling.strip()
        try:
            supervisor = li.find('strong', text='Научный руководитель:').next_sibling.strip()
        except:
            supervisor = 'Научный руководитель неизвестен'
        articles.append({'title': title, 'authors': authors, 'supervisor': supervisor})
    return articles