from django.contrib import admin
from .models import Article, ReadNext, Sidenav

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_title', 'article_category', 'article_author', 'article_pub_date', 'was_published_recently')
    list_filter = ['article_pub_date']
    search_fields = ['article_author', 'article_title']

class RNAdmin(admin.ModelAdmin):
    list_display = ('rn_nav_title', 'rn_title')
    search_fields = ['rn_nav_title']

class SidenavAdmin(admin.ModelAdmin):
    list_display = ('sidenav_title',)
    search_fields = ['sidenav_title']

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(ReadNext, RNAdmin)
admin.site.register(Sidenav, SidenavAdmin)
