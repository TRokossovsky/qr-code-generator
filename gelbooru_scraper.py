import json
import asyncio
from python_gelbooru import AsyncGelbooru

with open('./Testing/APIs.txt', 'r') as f:
    data = f.read()
    js = json.loads(data)
api_key, user_id = (js['api_key'], js['user_id'])


async def main():
    async with AsyncGelbooru(api_key=api_key,
                             user_id=user_id) as gel:
        yuyu = await gel.search_posts(['as109'], limit=999, random=True)

        tasks = [i.async_download(f"./arts/{i.id}") for i in yuyu]
        await asyncio.gather(*tasks)

while True:
    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())

# scraps up to 100 elements in a row. launch with random=True until it collects all.
