# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0025_auto_20160617_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(related_name='user_pro', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='upfile',
            name='status',
            field=models.CharField(max_length=10, verbose_name='审批', choices=[('等待审核', '等待审核'), ('等待再次审批', '等待再次审批'), ('审批通过', '审批通过'), ('审批不通过', '审批不通过')], default='等待审核'),
        ),
    ]
