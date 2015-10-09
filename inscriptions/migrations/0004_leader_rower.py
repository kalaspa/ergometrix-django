# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='leader',
            name='rower',
            field=models.ForeignKey(null=True, to='inscriptions.Rower'),
        ),
    ]
