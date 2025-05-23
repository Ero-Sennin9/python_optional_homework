import aiohttp
import asyncio

from parse_page_async import parse_page_async

async def async_parsing(pages_count):
    results = []
    async with aiohttp.ClientSession() as session:
        tasks = [parse_page_async(page, session) for page in range(pages_count)]
        results = await asyncio.gather(*tasks)
    return [item for sublist in results for item in sublist]

asyncio.run(async_parsing(20))
