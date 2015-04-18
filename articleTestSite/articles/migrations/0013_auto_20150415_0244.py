# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_auto_20150415_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_hero_image',
            field=models.ImageField(default='', upload_to='media/heroimg/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_optional_image',
            field=models.ImageField(default='', upload_to='media/subimg/', blank=True),
        ),
    ]
