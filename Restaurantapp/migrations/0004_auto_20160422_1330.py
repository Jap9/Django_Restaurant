# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurantapp', '0003_restaurant_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='price',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
