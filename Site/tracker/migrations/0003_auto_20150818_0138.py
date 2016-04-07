# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='PSC',
            field=models.CharField(default='Empty', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='mouse',
            field=models.CharField(default='C57BL6', max_length=255),
            preserve_default=False,
        ),
    ]
