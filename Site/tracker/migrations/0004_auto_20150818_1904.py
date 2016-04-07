# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20150818_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='endDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='startDate',
            field=models.DateField(),
        ),
    ]
