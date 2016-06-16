# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0009_upfile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='upfile',
            options={'verbose_name_plural': '文件上传', 'ordering': ('-created',), 'verbose_name': '文件上传'},
        ),
        migrations.AddField(
            model_name='upfile',
            name='reply',
            field=models.CharField(max_length=160, default='项目审核中', verbose_name='批复'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upfile',
            name='status',
            field=models.CharField(max_length=10, choices=[('审批通过', '审批通过'), ('审批不通过', '审批不通过')], default='审批不通过', verbose_name='审批'),
        ),
    ]
