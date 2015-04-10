import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Article


# Create your tests here.
"""
class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_article(self):
        "_""
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        "_""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Article(article_pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

def test_was_published_recently_with_old_article(self):
    "_""
    was_published_recently() should return False for questions whose
    pub_date is older than 1 day.
    "_""
    time = timezone.now() - datetime.timedelta(days=30)
    old_question = Article(article_pub_date=time)
    self.assertEqual(old_question.was_published_recently(), False)

def test_was_published_recently_with_recent_article(self):
    "_""
    was_published_recently() should return True for questions whose
    pub_date is within the last day.
    "_""
    time = timezone.now() - datetime.timedelta(hours=1)
    recent_question = Article(article_pub_date=time)
    self.assertEqual(recent_question.was_published_recently(), True)
    """