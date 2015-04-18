# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20150415_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_hero_image',
            field=models.ImageField(upload_to='/articleTestSite/articles/static/articles/images/heroimg/', default=''),
        ),
    ]
