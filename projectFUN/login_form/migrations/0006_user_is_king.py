# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_form', '0005_auto_20170325_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_king',
            field=models.BooleanField(default=False),
        ),
    ]