# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-06 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('slug', models.SlugField(verbose_name='atalho')),
                ('description', models.TextField(blank=True, verbose_name='descrição simples')),
                ('about', models.TextField(blank=True, verbose_name='sobre o curso')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='data de início')),
                ('image', models.ImageField(blank=True, null=True, upload_to='courses/images', verbose_name='imagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='atualizado em')),
            ],
            options={
                'verbose_name': 'curso',
                'db_table': 'courses',
                'verbose_name_plural': 'cursos',
                'ordering': ['name'],
            },
        ),
    ]
