# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wb', '0002_auto_20170722_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wbuser',
            name='password',
            field=models.CharField(max_length=150, verbose_name='密码'),
        ),
    ]
