from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /articles/
    url(r'^$', views.indexArticle, name='indexArticle'),
]