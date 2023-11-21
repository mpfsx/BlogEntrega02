from django.test import TestCase
from .models import Post
from django.utils import timezone
from django.urls import reverse

class PostModelTests(TestCase):

    def test_was_published_recently_with_future_post(self):
        """
        was_published_recently() returns False for posts whose pub_date
        is in the future.
        """
        time = timezone.now() + timezone.timedelta(days=30)
        future_post = Post(pub_date=time)
        self.assertIs(future_post.was_published_recently(), False)

    def test_was_published_recently_with_old_post(self):
        """
        was_published_recently() returns False for posts whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - timezone.timedelta(days=1, seconds=1)
        old_post = Post(pub_date=time)
        self.assertIs(old_post.was_published_recently(), False)

    def test_was_published_recently_with_recent_post(self):
        """
        was_published_recently() returns True for posts whose pub_date
        is within the last day.
        """
        time = timezone.now() - timezone.timedelta(hours=23, minutes=59, seconds=59)
        recent_post = Post(pub_date=time)
        self.assertIs(recent_post.was_published_recently(), True)

def create_post(title, days):
    """
    Create a post with the given `title` and published the given
    number of `days` offset to now (negative for posts published
    in the past, positive for posts that have yet to be published).
    """
    time = timezone.now() + timezone.timedelta(days=days)
    return Post.objects.create(title=title, pub_date=time)

class PostIndexViewTests(TestCase):

    def test_no_posts(self):
        """
        If no posts exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('app:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No posts are available.')
        self.assertQuerysetEqual(response.context['latest_post_list'], [])

    def test_past_post(self):
        """
        Posts with a pub_date in the past are displayed on the index page.
        """
        create_post(title='Past post.', days=-30)
        response = self.client.get(reverse('app:index'))
        self.assertQuerysetEqual(
            response.context['latest_post_list'],
            ['<Post: Past post.>']
        )

    def test_future_post(self):
        """
        Posts with a pub_date in the future should not be displayed on
        the index page.
        """
        create_post(title='Future post.', days=30)
        response = self.client.get(reverse('app:index'))
        self.assertContains(response, 'No posts are available.')
        self.assertQuerysetEqual(response.context['latest_post_list'], [])

    def test_future_post_and_past_post(self):
        """
        Even if both past and future posts exist, only past posts
        should be displayed.
        """
        create_post(title='Past post.', days=-30)
        create_post(title='Future post.', days=30)
        response = self.client.get(reverse('app:index'))
        self.assertQuerysetEqual(
            response.context['latest_post_list'],
            ['<Post: Past post.>']
        )

    def test_two_past_posts(self):
        """
        The posts index page may display multiple posts.
        """
        create_post(title='Past post 1.', days=-30)
        create_post(title='Past post 2.', days=-5)
        response = self.client.get(reverse('app:index'))
        self.assertQuerysetEqual(
            response.context['latest_post_list'],
            ['<Post: Past post 2.>', '<Post: Past post 1.>']
        )