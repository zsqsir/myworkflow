# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0010_auto_20160611_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='upfile',
            name='update',
            field=models.DateField(auto_now=True, verbose_name='修改时间', default=datetime.datetime(2016, 6, 11, 7, 52, 56, 691170, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='upfile',
            name='status',
            field=models.CharField(choices=[('等待审批', '等待审批'), ('等待再次审批', '等待再次审批'), ('审批通过', '审批通过'), ('审批不通过', '审批不通过')], max_length=10, verbose_name='审批', default='等待审核'),
        ),
    ]
