# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0002_auto_20141114_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='hEntrada',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='hSalida',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
