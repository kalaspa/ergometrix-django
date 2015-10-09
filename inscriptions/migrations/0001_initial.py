# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('record', models.IntegerField()),
                ('payment', models.BooleanField()),
                ('deleted', models.BooleanField()),
                ('valid', models.BooleanField()),
                ('created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(max_length=10)),
                ('club', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rower',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('lastname', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('license', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='boat',
            name='leader',
            field=models.ManyToManyField(to='inscriptions.Leader'),
        ),
        migrations.AddField(
            model_name='boat',
            name='rower',
            field=models.ManyToManyField(to='inscriptions.Rower'),
        ),
    ]
