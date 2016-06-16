# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0015_auto_20160615_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='update',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]
