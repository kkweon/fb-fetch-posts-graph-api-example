import json
from unittest import TestCase

from lib.models.post import Post


class TestPost(TestCase):
    def test_from_json(self):
        input_ = """
    {
      "message": "ABC",
      "updated_time": "2019-01-18T12:07:11+0000",
      "id": "292278624537271_613979992367131"
    }

        """
        post = Post.from_json(json.loads(input_))

        self.assertEqual(post.message, "ABC")
        self.assertEqual(post.id, "292278624537271_613979992367131")
