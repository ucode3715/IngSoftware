# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0002_parametros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametros',
            name='hEntrada',
            field=models.CharField(max_length=64, validators=[django.core.validators.RegexValidator(regex=b'(1[0-2]|[1-9]):[0-5][0-9](\\s)(a|p)m$', message=b'Debe una hora valida. Por Ejemplo: 9:00 am ')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='parametros',
            name='hSalida',
            field=models.CharField(max_length=64, validators=[django.core.validators.RegexValidator(regex=b'(1[0-2]|[1-9]):[0-5][0-9](\\s)(a|p)m$', message=b'Debe una hora valida. Por Ejemplo: 9:00 pm ')]),
            preserve_default=True,
        ),
    ]
