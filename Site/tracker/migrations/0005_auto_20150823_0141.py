# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20150818_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='endDate',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mouse',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='startDate',
            field=models.DateField(null=True, blank=True),
        ),
    ]
