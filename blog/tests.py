from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
class PostModelTest(TestCase):

    def setUp(self):
        self.user=User.objects.create_user(username="Nikhil",password='12345')

    def test_post_creation(self):
        post=Post.objects.create (
            title='this is my blog',
            content='I fell in love with python',
            author=self.user
            )
        self.assertEqual(post.title,'this is my blog')
        self.assertEqual(post.content,'I fell in love with python')
        self.assertEqual(post.author,self.user)
        self.assertIsNotNone(post.created_at)

    def test_post_string_representation(self):
        post = Post(title='this is my blog')
        self.assertEqual(str(post),'this is my blog')

    def test_post_ordering(self):
        post1=Post.objects.create(
            title='this is my title1',
            content='I love dhango',
            author=self.user,
        )
        post2=Post.objects.create(
            title='this is my title2',
            content='I love django and python',
            author=self.user,
        )
        post1.created_at=timezone.now()-timedelta(seconds=2)
        post2.created_at=timezone.now()-timedelta(seconds=1)

        post1.save()
        post2.save()

        posts=Post.objects.all()
        self.assertEqual(posts[0],post2)
        self.assertEqual(posts[1],post1)
        


