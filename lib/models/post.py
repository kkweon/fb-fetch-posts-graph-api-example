from __future__ import annotations

import datetime
from typing import List

from lib.models.like import Like


class Post(object):
    """
    글(Post)를 나타냅니다.
    """

    message: str
    updated_time: datetime.datetime
    id: str
    likes: List[Like]

    @classmethod
    def from_json(cls, message_json: dict) -> Post:
        m = Post()
        m.message = message_json.get("message", "")
        m.updated_time = datetime.datetime.strptime(
            message_json.get("updated_time"), "%Y-%m-%dT%H:%M:%S%z"
        )
        m.id = message_json.get("id")
        m.likes = []
        return m

    def __repr__(self) -> str:
        return f"Message(message={self.__get_message()}, likes={self.likes}, updated_time={self.updated_time}, id={self.id})"

    def __get_message(self) -> str:
        if len(self.message) < 10:
            return self.message

        return self.message[:7] + "..."
