# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-23 02:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operate', models.CharField(choices=[(1, '收藏'), (2, '取消收藏'), (3, '租赁')], max_length=10, verbose_name='操作')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创造时间')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户日志',
                'verbose_name_plural': '用户日志',
                'ordering': ['-create_time'],
            },
        ),
    ]
