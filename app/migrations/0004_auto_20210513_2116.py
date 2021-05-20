# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-13 18:16
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20210508_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(db_index=True, default=datetime.datetime(2021, 5, 13, 21, 16, 18, 748663), verbose_name='Дата')),
                ('ready', models.BooleanField(default=False, verbose_name='Статус')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказ',
                'db_table': 'Orders',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.CharField(max_length=100, verbose_name='Цена')),
                ('image', models.FileField(default='temp.jpg', upload_to='', verbose_name='Путь к картинке')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товар',
                'db_table': 'Products',
                'ordering': ['title'],
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.FileField(default='temp.jpg', upload_to='', verbose_name='Путь к изображению'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 5, 13, 21, 16, 18, 745662), verbose_name='Опубликована'),
        ),
        migrations.AddField(
            model_name='orders',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Products', verbose_name='Товар'),
        ),
    ]
