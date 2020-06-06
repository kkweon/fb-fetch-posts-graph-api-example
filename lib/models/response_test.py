import json
from unittest import TestCase

from lib.models.post import Post
from lib.models.response import Response


class TestResponse(TestCase):
    def test_from_json(self):
        input_ = """
{
  "data": [
    {
      "message": "Hi",
      "updated_time": "2019-01-18T12:07:11+0000",
      "id": "292278624537271_613979992367131"
    }
  ]
}
"""
        resp: Response[Post] = Response.from_json(json.loads(input_))
        self.assertEqual(len(resp.data), 1)
        self.assertIsInstance(resp.data[0], Post)
        self.assertEqual(resp.data[0].message, "Hi")
