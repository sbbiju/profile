# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-18 17:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_test', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='email',
        ),
    ]