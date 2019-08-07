from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        my_blog = Blog('BlogName', 'BlogAuthor')
        my_blog.create_post('PostTitle', 'PostContent')

        self.assertEqual(my_blog.posts[0].title, 'PostTitle')
        self.assertEqual(my_blog.posts[0].content, 'PostContent')

    def test_json(self):
        my_blog = Blog('BlogName', 'BlogAuthor')
        my_blog.create_post('PostTitle', 'PostContent')
        expected = {'title': 'BlogName',
                    'author': 'BlogAuthor',
                    'posts': [{'title': 'PostTitle',
                               'content': 'PostContent'}]}

        self.assertDictEqual(expected, my_blog.json())

    def test_json_no_posts(self):
        my_blog = Blog('BlogTitle', 'BlogAuthor')
        expected = {'title': 'BlogTitle', 'author': 'BlogAuthor', 'posts': []}

        self.assertDictEqual(expected, my_blog.json())
