# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_auto_20150415_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_thumbnail_optional',
            field=models.ImageField(upload_to='media/thumbnail/', default='', blank=True),
        ),
    ]
