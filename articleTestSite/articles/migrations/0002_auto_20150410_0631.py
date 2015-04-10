# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sidenav',
            name='sidenav_nav_title',
        ),
        migrations.AlterField(
            model_name='readnext',
            name='rn_nav_title',
            field=models.CharField(max_length=128),
        ),
    ]
