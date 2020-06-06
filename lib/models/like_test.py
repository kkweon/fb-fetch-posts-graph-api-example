import json
from unittest import TestCase

from lib.models.like import Like


class TestLike(TestCase):
    def test_from_json(self):
        input_ = """
{
  "id": "10163522886740632",
  "name": "Mo Kweon",
  "type": "LIKE"
}
"""
        like = Like.from_json(json.loads(input_))
        expected = Like()
        expected.id = "10163522886740632"
        expected.name = "Mo Kweon"
        expected.type = "LIKE"

        self.assertEqual(like, expected)
