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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('article_title', models.CharField(verbose_name='Title: ', max_length=256)),
                ('article_author', models.CharField(verbose_name='Author: ', max_length=128)),
                ('article_pub_date', models.DateTimeField(verbose_name='Date published')),
                ('article_category', models.CharField(verbose_name='Category: ', max_length=64)),
                ('article_body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ReadNext',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('rn_nav_title', models.CharField(max_length=64)),
                ('rn_title', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Sidenav',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('sidenav_nav_title', models.CharField(max_length=64)),
                ('sidenav_title', models.CharField(max_length=256)),
            ],
        ),
    ]
