# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-03 11:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='thread',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='threads.Thread', verbose_name='tópico'),
            preserve_default=False,
        ),
    ]
