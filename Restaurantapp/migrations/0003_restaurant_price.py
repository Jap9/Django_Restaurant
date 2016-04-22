# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurantapp', '0002_auto_20160422_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='price',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
