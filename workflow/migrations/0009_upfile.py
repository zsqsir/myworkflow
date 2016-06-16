# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workflow', '0008_reimbursement_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpFile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('file', models.FileField(upload_to='%Y/%m/%d/', verbose_name='文件')),
                ('detail', models.TextField(max_length=200, verbose_name='详情')),
                ('created', models.DateField(verbose_name='上传时间', auto_now_add=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='上传者')),
            ],
            options={
                'verbose_name_plural': '文件',
                'verbose_name': '文件',
                'ordering': ('-created',),
            },
        ),
    ]
