# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=20, verbose_name='部门', choices=[('业务部', '业务部'), ('财务部', '财务部')])),
                ('level', models.CharField(max_length=10, verbose_name='职位', choices=[('经理', '经理'), ('职员', '职员')])),
                ('person', models.OneToOneField(verbose_name='姓名', to=settings.AUTH_USER_MODEL, related_name='department')),
            ],
            options={
                'verbose_name': '行政部门',
                'verbose_name_plural': '行政部门',
            },
        ),
        migrations.CreateModel(
            name='Leave_application',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('start_date', models.DateField(verbose_name='开始时间')),
                ('finished_date', models.DateField(verbose_name='结束时间')),
                ('reason', models.TextField(verbose_name='请假因由')),
                ('status', models.CharField(max_length=10, verbose_name='申请状态', default='等待批准', choices=[('等待批准', '等待批准'), ('批准', '批准'), ('不批准', '不批准')])),
                ('reply', models.TextField(max_length=250, verbose_name='批复', blank=True)),
                ('department', models.CharField(max_length=20, verbose_name='部门', editable=False)),
                ('applicant', models.ForeignKey(verbose_name='申请人', to=settings.AUTH_USER_MODEL, related_name='leave_application')),
            ],
            options={
                'verbose_name': '请假',
                'verbose_name_plural': '请假',
            },
        ),
        migrations.CreateModel(
            name='Notices',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('created', models.DateTimeField(verbose_name='发布时间', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
            ],
            options={
                'verbose_name': '公告',
                'verbose_name_plural': '公告',
            },
        ),
    ]
