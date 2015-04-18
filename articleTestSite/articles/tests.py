import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Article


# Create your tests here.
class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_article(self):
        """  was_published_recently() should return False for questions whose pub_date is in the future  """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Article(article_pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

def test_was_published_recently_with_old_article(self):
    """  was_published_recently() should return False for questions whose pub_date is older than 1 day  """
    time = timezone.now() - datetime.timedelta(days=30)
    old_question = Article(article_pub_date=time)
    self.assertEqual(old_question.was_published_recently(), False)

def test_was_published_recently_with_recent_article(self):
    """  was_published_recently() should return True for questions whose pub_date is within the last day. """
    time = timezone.now() - datetime.timedelta(hours=1)
    recent_question = Article(article_pub_date=time)
    self.assertEqual(recent_question.was_published_recently(), True)

def create_article(article_title, days):
    """  Creates a question with the given ARTICLE_TITLE published given the number of DAYS offset to now 
    (- for published, + for not published yet)  """
    time = timezone.now() + datetime.timedelta(days = days)
    return Article.objects.create(article_title = article_title, article_pub_date = time)

class ArticleViewTests(TestCase):
    def test_index_view_with_no_article(self):
        """  If no questions exist, an appropriate message should be displayed.  """
        response = self.client.get(reverse('articles/index.html'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No articles are available.")
        self.assertQuerysetEqual(response.context['latest_article_list'], [])

    def test_index_view_with_a_past_article(self):
        """  Questions with a pub_date in the past should be displayed on the index page.  """
        create_article(article_title="Past Articles.", days=-30)
        response = self.client.get(reverse('articles/index.html'))  #may just be index.html i never did get namespace going.
        self.assertQuerysetEqual(
            response.context['latest_article_list'],
            ['<Article: Past article.>']
        )

    def test_index_view_with_a_future_article(self):
        """   Questions with a pub_date in the future should not be displayed on the index page. """
        create_article(article_title="Future article.", days=30)
        response = self.client.get(reverse('articles/index.html'))
        self.assertContains(response, "No articles are available.",
                            status_code=200)
        self.assertQuerysetEqual(response.context['latest_article_list'], [])

    def test_index_view_with_future_article_and_past_article(self):
        """   Even if both past and future articles exist, only past articles should be displayed. """
        create_article(article_title="Past article.", days=-30)
        create_article(article_title="Future article.", days=30)
        response = self.client.get(reverse('articles/index.html'))
        self.assertQuerysetEqual(
            response.context['latest_article_list'],
            ['<Article: Past article.>']
        )

    def test_index_view_with_two_past_articles(self):
        """  The ARTICLES index page may display multiple articles.  """
        create_article(article_title="Past article 1.", days=-30)
        create_article(article_title="Past article 2.", days=-5)
        response = self.client.get(reverse('articles/index.html'))
        self.assertQuerysetEqual(
            response.context['latest_article_list'],
            ['<Article: Past article 2.>', '<Article: Past article 1.>']
        )


class ArticleIndexArticleViewTests(TestCase):
    def test_article_view_with_a_future_article(self):
        """  The detail view of a article with a pub_date in the future should return a 404 not found. """
        future_article = create_article(article_title='Future article.', days=5)
        response = self.client.get(reverse('articles/index.html', args=(future_article.id,)))
        self.assertEqual(response.status_code, 404)

    def test_article_view_with_a_past_article(self):
        """   The detail view of a article with a pub_date in the past should display the article. """
        past_article = create_article(article_title='Past article.', days=-5)
        response = self.client.get(reverse('articles/index.html', args=(past_article.id,)))
        self.assertContains(response, past_article.article_title, status_code=200)