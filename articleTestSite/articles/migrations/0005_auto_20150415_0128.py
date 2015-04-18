# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_article_article_hero_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_hero_image',
            field=models.ImageField(default='', upload_to='articles/static/articles/images/heroimg/'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_optional_image',
            field=models.ImageField(default='', upload_to='articles/static/articles/images/subimg/'),
        ),
    ]
