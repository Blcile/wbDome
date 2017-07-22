# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wbuser',
            name='loginname',
            field=models.CharField(max_length=20, verbose_name='登陆名'),
        ),
        migrations.AlterField(
            model_name='wbuser',
            name='nickname',
            field=models.CharField(max_length=20, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='wbuser',
            name='password',
            field=models.CharField(max_length=50, verbose_name='密码'),
        ),
    ]
