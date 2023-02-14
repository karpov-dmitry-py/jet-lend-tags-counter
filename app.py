import logging
import asyncio

from bs4 import BeautifulSoup

import aiohttp

logging.basicConfig(level='INFO', format='[%(asctime)s] %(levelname)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

URL = 'https://jetlend.ru'


class Parser:

    @staticmethod
    def get_tag_count(html) -> (int, int):
        soup = BeautifulSoup(html, "html.parser")
        tags = [tag for tag in soup.find_all()]
        tag_with_attrs_count = sum([1 if tag.attrs else 0 for tag in tags])
        return len(tags), tag_with_attrs_count


class HttpClient:

    def __init__(self, url) -> None:
        self.__url = url

    async def process_url(self) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.__url) as response:
                html = await response.text()
                tag_count, tag_with_attrs_count = Parser.get_tag_count(html)
                logger.info(
                    f'tag stats for {self.__url}: tags total {tag_count}, tags with attrs: {tag_with_attrs_count}')
                await asyncio.sleep(60)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(HttpClient(url=URL).process_url())
