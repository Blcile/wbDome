# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 09:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wb', '0003_auto_20170722_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wbuser',
            name='loginname',
        ),
    ]
