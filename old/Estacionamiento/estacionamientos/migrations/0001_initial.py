# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Nombre', models.CharField(max_length=200)),
                ('RIF', models.CharField(max_length=10)),
                ('Encargado', models.CharField(max_length=11)),
                ('Telefono_1', models.IntegerField()),
                ('Telefono_2', models.IntegerField()),
                ('Telefono_3', models.IntegerField()),
                ('Correo_1', models.EmailField(max_length=100)),
                ('Correo_2', models.EmailField(max_length=100)),
                ('Puestos', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('ocupado', models.BooleanField()),
                ('Estacionamiento', models.ForeignKey(to='estacionamientos.Estacionamiento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
