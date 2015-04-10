import os
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    article_title = models.CharField("Title: ", max_length=256)
    article_author = models.CharField("Author: ", max_length=128)
    article_pub_date = models.DateTimeField("Date published")
    article_category = models.CharField("Category: ", max_length=64)
    #article_hero_image = ImageField(blank=True)
    #article_optional_image = ImageField(blank=True)  #BLANK=TRUE makes optional
    article_body = models.TextField()
    # USE IF CANT GET ABOVE WORKING, SET TO AN ARBITRARILY LONG CHAR VALUE 
    # article_body = models.CharField(max_length=65536)

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.article_pub_date >= timezone.now() - datetime.timedelta(days=9)
    was_published_recently.admin_order_field = 'article_pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class ReadNext(models.Model):
    rn_nav_title = models.CharField(max_length=128)
    rn_title = models.CharField(max_length=256)
    #rn_image = ImageField(blank=True)
    
    def __str__(self):   
        return self.rn_nav_title 

class Sidenav(models.Model):
    sidenav_title = models.CharField(max_length=256)
    #sidenav_image = ImageField(blank=True)

    def __str__(self):   
        return self.sidenav_title 