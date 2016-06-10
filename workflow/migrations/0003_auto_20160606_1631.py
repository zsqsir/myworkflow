# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workflow', '0002_auto_20160606_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='worksheet',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('description', models.TextField(max_length=300, verbose_name='情况说明')),
                ('who_is_processing', models.CharField(verbose_name='当前处理人', default='未知', max_length=20)),
                ('plan_finish_time', models.DateField(verbose_name='计划完成时间')),
                ('status_level', models.CharField(max_length=10, verbose_name='当前状态', default='修改中', choices=[('修改中', '修改中'), ('验证中', '验证中'), ('审批中', '审批中')])),
                ('department', models.CharField(max_length=20, verbose_name='部门')),
                ('creater', models.ForeignKey(verbose_name='创建人', related_name='worksheet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='leave_application',
            name='title',
            field=models.CharField(verbose_name='标题', default='q', max_length=50),
            preserve_default=False,
        ),
    ]
