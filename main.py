from __future__ import annotations

import asyncio
import os
import logging

import aiohttp

from lib.fb_client import FacebookClient
from lib.refresh_token import refresh_token

GROUP_ID = os.environ.get("FB_GROUP_ID")
ACCESS_TOKEN = os.environ.get("FB_ACCESS_TOKEN")
APP_ID = os.environ.get("FB_APP_ID")
APP_SECRET = os.environ.get("FB_APP_SECRET")

logging.basicConfig(level=logging.INFO)


async def main():
    token = await refresh_token(APP_ID, APP_SECRET, ACCESS_TOKEN)

    logging.info("token = %s", token)

    fb_client = FacebookClient(GROUP_ID, token.access_token)
    async with aiohttp.ClientSession() as session:
        posts = await fb_client.fetch_posts(session)
        print(posts)


if __name__ == "__main__":
    asyncio.run(main())
