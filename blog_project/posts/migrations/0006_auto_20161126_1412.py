# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-26 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_post',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
