from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.base import TemplateView
from django.utils import timezone
from .models import Article #, ReadNext, Sidenav

# Create your views here.
class HomePage(TemplateView):
	template_name = "articles/home.html"
	def get_context_data(self):
		context = super(HomePage, self).get_context_data()
		context['latest_article_list'] = Article.objects.all()[:5]
		return context


class ArticleLanding(generic.ListView):
	template_name = 'articles/index.html'
	context_object_name = 'latest_article_list'
	""" Return the last 4 published questions, NOT INCLUDING FUTURE ENTRIES """
	def get_queryset(self):
		return Article.objects.filter(article_pub_date__lte = timezone.now()).order_by('-article_pub_date')[:4]

class ArticleView(generic.DetailView):
	model = Article
	template_name = 'articles/articlePage.html'
	def get_queryset(self):
		"""  Excludes any articles that aren't published yet """
		return Article.objects.filter(article_pub_date__lte=timezone.now())


"""
#REFACTORED DOWN TO GENERIC VIEWS  -- TUTORIAL 4
def indexArticle(request):
    #use a function like this to display the most recent 4-5 articles for the READ NEXT and SIDENAV
    latest_article_list = Article.objects.order_by('-article_pub_date')[:4]
    context = {'latest_article_list' : latest_article_list,}
    return render(request, 'articles/index.html', context)

def showArticle(request, article_id):
	article = get_object_or_404(Article, pk=article_id)
	return render(request, 'articles/articlePage.html', {'article' : article})

 # Create your views here -- USE IF I WANT TO MAKE AN ARTICLE LANDING PAGE WITH ALL SHOWING
def indexArticle(request):
    response = "You're at the index for the sports section."
    return HttpResponse(response)
"""