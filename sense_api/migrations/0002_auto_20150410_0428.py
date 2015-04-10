# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sense_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locationlog',
            old_name='device_id',
            new_name='device',
        ),
    ]
