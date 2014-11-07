# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('capacidad', models.IntegerField()),
                ('hEntrada', models.CharField(max_length=64, validators=[django.core.validators.RegexValidator(regex=b'(1[0-2]|[1-9]):[0-5][0-9](\\s)?(a|p)m$', message=b'Debe una hora valida. Por Ejemplo: 9:00 am ')])),
                ('hSalida', models.CharField(max_length=64, validators=[django.core.validators.RegexValidator(regex=b'(1[0-2]|[1-9]):[0-5][0-9](\\s)?(a|p)m$', message=b'Debe una hora valida. Por Ejemplo: 9:00 pm ')])),
                ('tarifa', models.DecimalField(max_digits=1000, decimal_places=2)),
                ('estacionamiento', models.ForeignKey(to='estacionamientos.Estacionamiento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
