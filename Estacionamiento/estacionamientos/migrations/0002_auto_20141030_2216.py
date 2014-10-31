# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamientos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puesto',
            name='ocupado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
