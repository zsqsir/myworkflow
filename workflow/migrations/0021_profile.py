# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workflow', '0020_auto_20160616_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nickname', models.CharField(max_length=10, blank=True, verbose_name='昵称')),
                ('date_of_birth', models.DateField(blank=True, verbose_name='生日')),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d', verbose_name='图片')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '个人资料',
                'verbose_name': '个人资料',
            },
        ),
    ]
