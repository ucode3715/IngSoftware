# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0003_auto_20141114_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametros',
            name='hEntrada',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parametros',
            name='hSalida',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
