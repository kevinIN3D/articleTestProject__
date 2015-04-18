# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20150415_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_hero_image',
            field=models.ImageField(upload_to='articles/images/heroimg', default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_optional_image',
            field=models.ImageField(upload_to='articles/images/subimg/', default='', blank=True),
        ),
    ]
