# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('summary', models.CharField(max_length=128, verbose_name='タスク')),
                ('complete', models.BooleanField(default=False, verbose_name='状態')),
                ('comment', models.CharField(blank=True, max_length=512, verbose_name='コメント')),
                ('done_date', models.DateField(blank=True, null=True, verbose_name='完了日')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='tasks')),
            ],
        ),
    ]
