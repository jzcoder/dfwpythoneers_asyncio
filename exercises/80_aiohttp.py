"""
Use third-party async HTTP library

...
"""
import asyncio, demo, aiohttp

async def fetch(session, url):
    with aiohttp.Timeout(10, loop=session.loop):
        async with session.get(url) as response:
            return url, response.status, response.content_length

async def main(loop):
    async with aiohttp.ClientSession(loop=loop) as session:

        results = await asyncio.gather(fetch(session, 'http://python.org'),
                                       fetch(session, 'http://www.google.com'),
                                       fetch(session, 'http://pypi.python.org/pypi'))

        for result in results:
            demo.LOG(f'url={result[0]} status={result[1]} length={result[2]}')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))