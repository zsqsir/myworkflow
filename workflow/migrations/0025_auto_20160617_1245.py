# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0024_auto_20160617_1240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('-created',), 'verbose_name_plural': '站内短消息', 'verbose_name': '站内短消息'},
        ),
    ]
