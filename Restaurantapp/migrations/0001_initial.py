# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('DNI', models.CharField(max_length=9)),
                ('age', models.IntegerField()),
                ('date', models.DateField(default=datetime.date.today)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('telephone', models.TextField(null=True, blank=True)),
                ('street', models.TextField(null=True, blank=True)),
                ('city', models.TextField(default=b'')),
                ('zipCode', models.TextField(null=True, blank=True)),
                ('web', models.URLField(null=True, blank=True)),
                ('free', models.IntegerField(null=True, blank=True)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
