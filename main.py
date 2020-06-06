from __future__ import annotations

import asyncio
import os
import aiohttp

from fb_client import FacebookClient

GROUP_ID = os.environ.get("FB_GROUP_ID")
ACCESS_TOKEN = os.environ.get("FB_ACCESS_TOKEN")


async def main():
    fb_client = FacebookClient(GROUP_ID, ACCESS_TOKEN)
    async with aiohttp.ClientSession() as session:
        posts = await fb_client.fetch_posts(session)
        print(posts)


if __name__ == '__main__':
    asyncio.run(main())
