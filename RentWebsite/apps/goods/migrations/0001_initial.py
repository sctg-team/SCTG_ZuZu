# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-22 13:15
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='分类名称')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='商品标题')),
                ('desc', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='物品描述')),
                ('rent', models.DecimalField(decimal_places=10, max_digits=11, verbose_name='租金')),
                ('deposit', models.DecimalField(decimal_places=10, max_digits=11, verbose_name='押金')),
                ('pub_time', models.DateTimeField(auto_now_add=True, verbose_name='入库时间')),
                ('status', models.BooleanField(default=False, verbose_name='审核状态')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Category', verbose_name='所属分类')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'permissions': (('can_change_good', '可以修改商品信息'), ('can_add_good', '可以添加商品信息'), ('can_change_good_status', '可以修改商品状态')),
            },
        ),
        migrations.CreateModel(
            name='GoodsCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='收藏/取消时间')),
                ('status', models.BooleanField(default=True, verbose_name='收藏状态')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_collection_set', to='goods.Goods', verbose_name='出租物品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_collection_set', to=settings.AUTH_USER_MODEL, verbose_name='收藏者')),
            ],
            options={
                'verbose_name': '收藏记录',
                'verbose_name_plural': '收藏记录',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='标签名')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='tag',
            field=models.ManyToManyField(to='goods.Tag', verbose_name='商品标签'),
        ),
        migrations.AddField(
            model_name='goods',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='贡献者'),
        ),
    ]
