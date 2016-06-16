# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0014_remove_upfile_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='file_all',
            new_name='file_name',
        ),
    ]
