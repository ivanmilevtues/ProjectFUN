# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_form', '0003_auto_20170325_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
