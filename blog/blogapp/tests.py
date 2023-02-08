from django.test import TestCase

# Create your tests here.
from .models import Post, Category
from usersapp.models import BlogUser
class PostTestCase(TestCase):
    def test_has_image(self):
        category = Category.objects.create(name = 'test_category')
        user = BlogUser.objects.create_user(username = 'test_user', email = 'Q@QQ.ru', password = 'Django123')
        post = Post.objects.create(name = 'test_post', text = 'some', user = user, category = category)
        self.assertFalse(post.has_image())
    def test_some_method(self):
        category = Category.objects.create(name = 'test_category')
        user = BlogUser.objects.create_user(username = 'test_user', email = 'Q@QQ.ru', password = 'Django123')
        post = Post.objects.create(name = 'test_post', text = 'some', user = user, category = category)
        self.assertFalse(post.some_method() == 'some method1')