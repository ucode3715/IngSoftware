# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='hEntrada',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reserva',
            name='hSalida',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
