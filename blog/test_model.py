import os
import django
import sys

# Add the project root to Python path
sys.path.append('C:/Users/jayak/projects/telsuko')

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telsuko.settings')
django.setup()   

import pytest
from blog.models import Post
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

pytestmark=pytest.mark.django_db

@pytest.fixture
def user():
    return User.objects.create_user(username="test_user",password='secreate')
@pytest.fixture
def post(user):
    return Post.objects.create(
        title="this is my app",
        content="this is python+django world",
        author=user
    )

def test_post_creation(post):
    assert post.title == "this is my app" 
    assert post.content== "this is python+django world"
    assert post.author.username == "test_user"
    assert isinstance(post.created_at,timezone.datetime)
    assert post.created_at <=timezone.now()

def test_post_string_representation(post):
    assert str(post) == "this is my app"

def test_post_ordering(user):

    #now=timezone.now()

    post1=Post.objects.create(
        title="hello",
        content="hey python",
        author=user,
        #created_at=now-timedelta(minutes=2),
    )
    post2 =Post.objects.create(
        title="helloo",
        content='hey django',
        author=user,
       # created_at=now-timedelta(minutes=1),
    )

    posts=Post.objects.all()

    assert posts[0]==post2
    assert posts[1]==post1