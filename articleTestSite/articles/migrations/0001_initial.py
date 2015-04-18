# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('article_title', models.CharField(max_length=256, verbose_name='Title: ')),
                ('article_author', models.CharField(max_length=128, verbose_name='Author: ')),
                ('article_pub_date', models.DateTimeField(verbose_name='Date published')),
                ('article_category', models.CharField(max_length=64, verbose_name='Category: ')),
                ('article_hero_image', models.ImageField(upload_to='articles/images/heroimg/', default='articles/images/heroimg/Hero.jpg')),
                ('article_body', models.TextField()),
            ],
        ),
    ]
