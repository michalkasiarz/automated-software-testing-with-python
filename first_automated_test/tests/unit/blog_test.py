from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        my_blog = Blog('BlogName', 'BlogAuthor')

        self.assertEqual('BlogName', my_blog.title)
        self.assertEqual('BlogAuthor', my_blog.author)
        self.assertListEqual([], my_blog.posts)

    def test_repr(self):
        my_blog = Blog('BlogName', 'BlogAuthor')

        self.assertEqual(my_blog.__repr__(), 'BlogName by BlogAuthor (0 posts)')

    def test_repr_one_post(self):
        my_blog = Blog('BlogName', 'BlogAuthor')
        my_blog.posts = ['jeden wesoły post']

        self.assertEqual(my_blog.__repr__(), 'BlogName by BlogAuthor (1 post)')

    def test_repr_multiple_posts(self):
        my_blog = Blog('BlogName', 'BlogAuthor')
        my_blog.posts = ['siema', 'elo', 'co tam', 'yo-man', 'nowy post']

        self.assertEqual(my_blog.__repr__(), 'BlogName by BlogAuthor (5 posts)')

