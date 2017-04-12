# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0005_auto_20170405_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='acertijo',
            name='respondido',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='opcion',
            name='correcto',
            field=models.BooleanField(default=False),
        ),
    ]
