from __future__ import annotations

from typing import Literal


class Like(object):
    """
    한 포스트의 Reaction 을 나타냄.
    """
    id: str
    name: str
    type: Literal[
        'NONE',
        'LIKE',
        'LOVE',
        'WOW',
        'HAHA',
        'SAD',
        'ANGRY',
        'THANKFUL',
        'PRIDE',
        'CARE',
    ]

    @classmethod
    def from_json(cls, like_json: dict) -> Like:
        like = Like()
        like.id = like_json.get('id')
        like.name = like_json.get('name')
        like.type = like_json.get('type')
        return like

    def __repr__(self) -> str:
        return f"Like(id={self.id}, name={self.name}, type={self.type})"
