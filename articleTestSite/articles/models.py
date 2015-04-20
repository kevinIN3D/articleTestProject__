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
    article_hero_image = models.ImageField(upload_to="media/heroimg/", default='')
    article_optional_image = models.ImageField(upload_to="media/subimg/", blank=True, default='')
    article_thumbnail_optional = models.ImageField(upload_to="media/thumbnail/", blank=True, default='')
    article_body = models.TextField()

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.article_pub_date <= now
    was_published_recently.admin_order_field = 'article_pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

