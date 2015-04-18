# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_hero_image',
            field=models.ImageField(default='', upload_to='/articles/images/heroimg/'),
        ),
    ]
