from unittest import TestCase
from post import Post


class PostTest(TestCase):
    def test_create_post(self):
        my_post = Post('TitleOfMyPost', 'ContentOfMyPost')

        self.assertEqual('TitleOfMyPost', my_post.title)
        self.assertEqual('ContentOfMyPost', my_post.content)

    def test_json(self):

        another_post = Post('Test Title', 'Test Content')
        expected = {'title': 'Test Title', 'content': 'Test Content'}

        self.assertDictEqual(expected, another_post.json())

