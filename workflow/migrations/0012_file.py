# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0011_auto_20160611_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('file_all', models.FileField(upload_to='%Y/%m/%d/', verbose_name='文件集')),
                ('file_title', models.ForeignKey(related_name='file_all', verbose_name='文件标题', to='workflow.UpFile')),
            ],
        ),
    ]
