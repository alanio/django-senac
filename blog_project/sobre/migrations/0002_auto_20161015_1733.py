# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-15 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sobre', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sobre',
            name='descricao',
            field=models.TextField(verbose_name='Descricao'),
        ),
    ]