from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from random import random, randint
from django.views.generic.base import TemplateView
from django.utils import timezone
from .models import Article #, ReadNext, Sidenav

# Create your views here.
class HomePage(TemplateView):
	template_name = "articles/home.html"


class ArticleLanding(generic.ListView):
	template_name = 'articles/index.html'
	context_object_name = 'latest_article_list'

	def get_queryset(self):
		random_index = randint(0, Article.objects.count() - 3)
		self.random_article = Article.objects.filter(article_pub_date__lte=timezone.now())[random_index]
		self.full_article_list = Article.objects.filter(article_pub_date__lte=timezone.now()).order_by('?')	#because our database is small, okay to sort using '?' which randomly sorts.  Not good for MEDIUM/LARGE databases, very memory heavy
		return Article.objects.filter(article_pub_date__lte = timezone.now()).order_by('-article_pub_date')[:4]
	def get_context_data(self, **kwargs):
		context = super(ArticleLanding, self).get_context_data(**kwargs)
		context['random_article'] = self.random_article
		context['full_article_list'] = self.full_article_list		
		return context

class ArticleView(generic.DetailView):
	model = Article
	template_name = 'articles/articlePage.html'
	def get_queryset(self):
		self.latest_article_list = Article.objects.filter(article_pub_date__lte=timezone.now()).order_by('-article_pub_date')[:4]
		self.full_article_list = Article.objects.filter(article_pub_date__lte=timezone.now()).order_by('?')
		return Article.objects.filter(article_pub_date__lte=timezone.now())
	def get_context_data(self, **kwargs):
		context = super(ArticleView, self).get_context_data(**kwargs)
		context['latest_article_list'] = self.latest_article_list
		context['full_article_list'] = self.full_article_list
		return context

