# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workflow', '0016_auto_20160615_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('status', models.IntegerField(verbose_name='状态', default=0)),
                ('title', models.CharField(verbose_name='标题', max_length=300)),
                ('content', models.TextField(verbose_name='内容')),
                ('created', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('marks', models.DateTimeField(verbose_name='标记', default=django.utils.timezone.now)),
                ('from_user', models.ForeignKey(verbose_name='发送者', to=settings.AUTH_USER_MODEL, related_name='sender')),
                ('to_user', models.ForeignKey(verbose_name='接收者', to=settings.AUTH_USER_MODEL, related_name='accepter')),
            ],
            options={
                'verbose_name_plural': '站内短消息',
                'verbose_name': '站内短消息',
                'ordering': ('-created',),
            },
        ),
    ]
