from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Article, ReadNext, Sidenav

# Create your views here.
def indexArticle(request):
    return HttpResponse("You're reading the sports section -- Article.")