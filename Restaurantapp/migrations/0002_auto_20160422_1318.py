# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurantapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='free',
            field=models.CharField(max_length=2, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='telephone',
            field=models.CharField(max_length=9, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='web',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='zipCode',
            field=models.TextField(max_length=5, null=True, blank=True),
        ),
    ]
