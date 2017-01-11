# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-11 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20170111_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('description', models.TextField(blank=True, verbose_name='descrição')),
                ('number', models.IntegerField(blank=True, default=0, verbose_name='número (ordem)')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='data de liberação')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='atualizado em')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.Course', verbose_name='curso')),
            ],
            options={
                'verbose_name': 'aula',
                'ordering': ['number'],
                'verbose_name_plural': 'aulas',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('embedded', models.TextField(blank=True, verbose_name='vídeo embedded')),
                ('file', models.FileField(blank=True, null=True, upload_to='lessons/materials', verbose_name='arquivo')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='courses.Lesson', verbose_name='aula')),
            ],
            options={
                'verbose_name': 'material',
                'verbose_name_plural': 'materiais',
            },
        ),
    ]
