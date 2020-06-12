from __future__ import annotations

import asyncio
import logging
from typing import List

import aiohttp

from lib.models.like import Like
from lib.models.post import Post
from lib.models.response import Response

BASE_URL = "https://graph.facebook.com/v7.0/"


def get_url(path: str, access_token: str) -> str:
    """Returns a FB API URL"""
    return BASE_URL + path + f"?access_token={access_token}"


class FacebookClient(object):
    group_id: str
    access_token: str

    def __init__(self, group_id: str, access_token: str):
        self.group_id = group_id
        self.access_token = access_token

    async def fetch_posts(self, session: aiohttp.ClientSession) -> List[Post]:
        """Fetch List[Post] and wraps with Response[Post]."""
        resp = await self.__fetch_posts_without_likes(session)
        if not resp:
            return []
        posts = await asyncio.gather(
            *[self.__fetch_like_for_post(session, post) for post in resp.data]
        )
        return posts

    async def __fetch_posts_without_likes(
        self, session: aiohttp.ClientSession
    ) -> Response[Post]:
        """Returns a response from GET /:group_id/feed."""
        async with session.get(
            get_url(f"/{self.group_id}/feed", self.access_token)
        ) as response:
            try:
                json_str = await response.json()
                return Response.from_json(json_str)

            except Exception as e:
                logging.critical("GET /:group_id/feed request has failed. Exception => %s", e)

    async def __fetch_like_for_post(
        self, session: aiohttp.ClientSession, post: Post
    ) -> Post:
        """Populate likes field in Post using GET /:object_id/reactions."""
        async with session.get(
            get_url(f"/{post.id}/reactions", self.access_token)
        ) as response:
            try:
                json_d = await response.json()
                data = json_d.get("data", [])

                for like_json in data:
                    like = Like.from_json(like_json)
                    post.likes.append(like)

            except Exception as err:
                logging.critical("get_like has failed. err = %s", err)

            return post
