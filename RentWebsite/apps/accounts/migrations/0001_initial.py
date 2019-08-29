# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-23 07:21

from __future__ import unicode_literals

import apps.goods.validator
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('realname', models.CharField(max_length=8, verbose_name='真实姓名')),
                ('sex', models.CharField(choices=[(0, '男'), (1, '女'), (None, '隐藏')], default=None, max_length=4, validators=[apps.goods.validator.valid_sex], verbose_name='性别')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机号')),
                ('qq', models.CharField(max_length=11, verbose_name='QQ号')),
                ('id_card', models.CharField(max_length=18, verbose_name='身份证号')),
                ('address', models.CharField(max_length=128, verbose_name='地址')),
                ('avator_sor', easy_thumbnails.fields.ThumbnailerImageField(default='avator/default.jpg', upload_to='avator/%Y%m%d/', verbose_name='头像')),
                ('avator_sm', models.ImageField(default='avator/5.70x70.jpg', upload_to='avator/%Y%m%d/', verbose_name='头像缩略图')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
