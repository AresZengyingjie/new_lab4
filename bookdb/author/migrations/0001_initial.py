# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AuthorID', models.CharField(max_length=60, verbose_name=b'AuthorID(PK)')),
                ('Name', models.CharField(max_length=60, verbose_name=b'Name', blank=True)),
                ('Age', models.CharField(max_length=10, verbose_name=b'Age', blank=True)),
                ('Country', models.CharField(max_length=60, verbose_name=b'Country', blank=True)),
            ],
            options={
                'verbose_name': 'Authors',
                'verbose_name_plural': 'Authors',
            },
        ),
    ]
