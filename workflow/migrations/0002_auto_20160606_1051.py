# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave_application',
            name='department',
            field=models.CharField(verbose_name='部门', max_length=20),
        ),
    ]
