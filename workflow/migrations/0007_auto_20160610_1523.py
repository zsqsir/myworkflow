# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0006_reimbursement'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reimbursement',
            options={'verbose_name_plural': '报销管理', 'verbose_name': '报销管理'},
        ),
        migrations.AlterField(
            model_name='reimbursement',
            name='status',
            field=models.CharField(max_length=20, verbose_name='审批状态', default='未核准'),
        ),
    ]
