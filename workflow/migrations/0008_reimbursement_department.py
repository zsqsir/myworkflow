# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0007_auto_20160610_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='reimbursement',
            name='department',
            field=models.CharField(verbose_name='部门', max_length=10, default='业务部'),
            preserve_default=False,
        ),
    ]
