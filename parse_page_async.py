import aiohttp
import asyncio
from bs4 import BeautifulSoup
import ssl

async def parse_page_async(page, session):
    url = f"https://nauchforum.ru/archive/article/all?page={page}"
    headers = {"User-Agent": "Mozilla/5.0"}

    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    successful_request = False
    while not successful_request:
        async with session.get(url, headers=headers, ssl=ssl_context) as response:
            if response.status == 200:
                successful_request = True
            text = await response.text()

            soup = BeautifulSoup(text, 'html.parser')
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