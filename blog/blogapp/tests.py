from django.test import TestCase

# Create your tests here.
from .models import Post, Category
from usersapp.models import BlogUser
class PostTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name = 'test_category')
        self.user = BlogUser.objects.create_user(username = 'test_user', email = 'Q@QQ.ru', password = 'Django123')
        self.post = Post.objects.create(name = 'test_post', text = 'some', user = self.user, category = self.category)

    def test_has_image(self):
        self.assertFalse(self.post.has_image())
    def test_some_method(self):
        post = Post.objects.get(name = 'test_post')
        self.assertFalse(self.post.some_method() == 'some method1')

    def test_str(self):
        self.assertEqual(str(self.post_str), 'test_post_str, category: test_category')