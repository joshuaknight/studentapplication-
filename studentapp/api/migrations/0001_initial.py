# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll_no', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30, choices=[(b'Male', 1), (b'Female', 2)])),
            ],
        ),
    ]
