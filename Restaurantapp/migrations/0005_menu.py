# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurantapp', '0004_auto_20160422_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codi_menu', models.TextField()),
                ('descripcio', models.TextField()),
                ('calories', models.IntegerField()),
            ],
        ),
    ]
