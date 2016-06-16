# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0019_auto_20160616_1159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name_plural': '站内短消息', 'verbose_name': '站内短消息', 'ordering': ('created',)},
        ),
        migrations.RemoveField(
            model_name='message',
            name='status',
        ),
        migrations.AddField(
            model_name='message',
            name='accept_msg_status',
            field=models.IntegerField(default=1, verbose_name='收信状态'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender_msg_status',
            field=models.IntegerField(default=1, verbose_name='发信状态'),
        ),
        migrations.AlterField(
            model_name='message',
            name='marks',
            field=models.CharField(max_length=20, verbose_name='标记'),
        ),
    ]
