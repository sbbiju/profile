# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-18 17:06
from __future__ import unicode_literals

from django.db import migrations, models
import my_test.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=80, null=True)),
                ('image', models.ImageField(upload_to=my_test.models.image_upload_to)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
