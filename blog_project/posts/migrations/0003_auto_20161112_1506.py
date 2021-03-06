# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-12 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20161029_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Categoria')),
                ('obs', models.TextField(blank=True, verbose_name='Observação')),
            ],
            options={
                'verbose_name': 'Categoria',
                'ordering': ['-id'],
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
