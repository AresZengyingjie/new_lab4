# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ISBN', models.CharField(unique=True, max_length=13, verbose_name=b'ISBN(PK)')),
                ('Title', models.CharField(max_length=200, verbose_name=b'Title')),
                ('AuthorID', models.CharField(max_length=60, verbose_name=b'AuthorID(FK)')),
                ('Price', models.CharField(max_length=60, verbose_name=b'Price', blank=True)),
                ('Publisher', models.CharField(max_length=200, verbose_name=b'Publisher', blank=True)),
                ('PublishDate', models.CharField(max_length=60, verbose_name=b'PublishDate', blank=True)),
                ('Summary', models.TextField(max_length=2000, verbose_name=b'Summary', blank=True)),
            ],
            options={
                'verbose_name': 'books',
                'verbose_name_plural': 'books',
            },
        ),
    ]
