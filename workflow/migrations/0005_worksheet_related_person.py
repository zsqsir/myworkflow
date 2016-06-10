# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0004_auto_20160606_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='worksheet',
            name='related_person',
            field=models.CharField(max_length=100, default='啊', verbose_name='相关人员'),
            preserve_default=False,
        ),
    ]
