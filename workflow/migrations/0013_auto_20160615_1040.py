# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0012_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'ordering': ('-update',), 'verbose_name_plural': '文件更新', 'verbose_name': '文件更新'},
        ),
        migrations.RenameField(
            model_name='file',
            old_name='file_title',
            new_name='file_id',
        ),
        migrations.AddField(
            model_name='file',
            name='update',
            field=models.DateField(auto_now=True, default=datetime.datetime(2016, 6, 15, 2, 40, 55, 866144, tzinfo=utc), verbose_name='更新时间'),
            preserve_default=False,
        ),
    ]
