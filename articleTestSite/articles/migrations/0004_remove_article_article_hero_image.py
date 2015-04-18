# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20150415_0103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_hero_image',
        ),
    ]
