# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20150415_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_hero_image',
            field=models.ImageField(default='', upload_to='../articles/images/heroimg/'),
        ),
    ]
