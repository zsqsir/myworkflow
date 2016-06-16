# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0018_auto_20160616_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='marks',
            field=models.CharField(default='20160616115933', max_length=20, verbose_name='标记'),
        ),
    ]
