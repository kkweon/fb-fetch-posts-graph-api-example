from __future__ import annotations

import asyncio
import logging
import os

import aiohttp

from lib.fb_client import FacebookClient
from lib.utils.token_service import build_access_token

logging.basicConfig(level=logging.DEBUG)

GROUP_ID = os.environ.get("FB_GROUP_ID")
ACCESS_TOKEN = os.environ.get("FB_ACCESS_TOKEN")


async def main():
    global ACCESS_TOKEN

    if not ACCESS_TOKEN:
        APP_ID = os.environ.get("FB_APP_ID")
        APP_SECRET = os.environ.get("FB_APP_SECRET")
        ACCESS_TOKEN = await build_access_token(APP_ID, APP_SECRET)

    if not ACCESS_TOKEN:
        raise EnvironmentError("ACCESS_TOKEN is not found. Please set environment variables FB_ACCESS_TOKEN or (both "
                               "FB_APP_ID and FB_APP_SECRET)")

    if not GROUP_ID:
        raise EnvironmentError("FB_GROUP_ID environment variable is not found")

    fb_client = FacebookClient(GROUP_ID, ACCESS_TOKEN)
    async with aiohttp.ClientSession() as session:
        posts = await fb_client.fetch_posts(session)
        print(posts)


if __name__ == "__main__":
    asyncio.run(main())
