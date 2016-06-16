# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0013_auto_20160615_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upfile',
            name='file',
        ),
    ]
