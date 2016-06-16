# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0017_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='from_user',
            field=models.ForeignKey(related_name='sender', to=settings.AUTH_USER_MODEL, verbose_name='发件人'),
        ),
        migrations.AlterField(
            model_name='message',
            name='marks',
            field=models.CharField(default='20160616034451', max_length=20, verbose_name='标记'),
        ),
        migrations.AlterField(
            model_name='message',
            name='to_user',
            field=models.ForeignKey(related_name='accepter', to=settings.AUTH_USER_MODEL, verbose_name='收件人'),
        ),
    ]
