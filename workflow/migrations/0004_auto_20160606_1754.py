# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0003_auto_20160606_1631'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='worksheet',
            options={'verbose_name_plural': '工单', 'verbose_name': '工单'},
        ),
        migrations.AddField(
            model_name='worksheet',
            name='create_time',
            field=models.DateField(verbose_name='创建时间', auto_now_add=True, default=datetime.datetime(2016, 6, 6, 9, 54, 22, 428989, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
