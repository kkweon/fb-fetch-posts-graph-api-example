from __future__ import annotations

from typing import Generic, List, TypeVar

from lib.models.post import Post

T = TypeVar("T")


class Response(Generic[T]):
    """
    This is a Response object when fetching the group feed.
    """

    data: List[T]

    def __init__(self):
        self.data = []

    @classmethod
    def from_json(cls, response_json: dict) -> Response[T]:
        resp = Response()
        resp.data = list(map(Post.from_json, response_json.get("data")))

        return resp
