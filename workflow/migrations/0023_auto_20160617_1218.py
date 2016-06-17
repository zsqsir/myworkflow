# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0022_auto_20160617_1143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name_plural': '站内短消息', 'ordering': ('-created',), 'verbose_name': '站内短消息'},
        ),
    ]
