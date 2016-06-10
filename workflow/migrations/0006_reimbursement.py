# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workflow', '0005_worksheet_related_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='reimbursement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('titile', models.CharField(verbose_name='报销单', max_length=30, default='报销')),
                ('start_date', models.DateField(verbose_name='开始时间')),
                ('end_date', models.DateField(verbose_name='结束时间')),
                ('description', models.TextField(help_text='报销的内容', max_length=300, verbose_name='情况说明')),
                ('money', models.FloatField(verbose_name='金额')),
                ('status', models.SlugField(default='未核准', verbose_name='审批状态')),
                ('reimbursement_person', models.ForeignKey(verbose_name='报销人', related_name='reimbursement', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
