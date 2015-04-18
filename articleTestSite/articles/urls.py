from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /articles/
    url(r'^$', views.ArticleLanding.as_view(), name='indexArticle'),
    url(r'^(?P<pk>[0-9]+)/$', views.ArticleView.as_view(), name='showArticle'),
]