# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('propietario', models.CharField(max_length=64, validators=[django.core.validators.RegexValidator(regex=b'^( |[a-zA-Z])*$', message=b'Debe ser un nombre de persona')])),
                ('nombre_est', models.CharField(max_length=64)),
                ('dir_est', models.CharField(max_length=256)),
                ('telf1', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(regex=b'^0(212|4(1(2|4|6)|2(4|6)))-?[1-9][0-9][0-9][0-9][0-9][0-9][0-9]$', message=b'Debe ser un telefono de ccs o de celular. Por Ejemplo: 0212-1234567')])),
                ('telf2', models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(regex=b'^0(212|4(1(2|4|6)|2(4|6)))-?[1-9][0-9][0-9][0-9][0-9][0-9][0-9]$', message=b'Debe ser un telefono de ccs o de celular. Por Ejemplo: 0212-1234567')])),
                ('telf3', models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator(regex=b'^0(212|4(1(2|4|6)|2(4|6)))-?[1-9][0-9][0-9][0-9][0-9][0-9][0-9]$', message=b'Debe ser un telefono de ccs o de celular. Por Ejemplo: 0212-1234567')])),
                ('email1', models.EmailField(max_length=75)),
                ('email2', models.EmailField(max_length=75, blank=True)),
                ('rif', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(regex=b'^(j|J|v|V|e|E|g|G|p|P)-?[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]-?[0-9]$', message=b'Debe ser un rif valido. Por Ejemplo: V-12345678-8')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parametros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('capacidad', models.IntegerField()),
                ('hEntrada', models.CharField(max_length=64, validators=[django.core.validators.RegexValidator(regex=b'(1[0-2]|[1-9]):[0-5][0-9](\\s)(a|p)m$', message=b'Debe una hora valida. Por Ejemplo: 9:00 am ')])),
                ('hSalida', models.CharField(max_length=64, validators=[django.core.validators.RegexValidator(regex=b'(1[0-2]|[1-9]):[0-5][0-9](\\s)(a|p)m$', message=b'Debe una hora valida. Por Ejemplo: 9:00 pm ')])),
                ('tarifa', models.DecimalField(max_digits=1000, decimal_places=2)),
                ('estacionamiento', models.OneToOneField(to='estacionamientos.Estacionamiento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estacionamiento', models.ForeignKey(to='estacionamientos.Estacionamiento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
