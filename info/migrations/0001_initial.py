# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonBasic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='PersonHealth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateOfBirth', models.DateField()),
                ('height', models.DecimalField(default=Decimal('0.00'), max_digits=20, decimal_places=2)),
                ('weight', models.DecimalField(default=Decimal('0.00'), max_digits=20, decimal_places=2)),
                ('person', models.ForeignKey(to='info.PersonBasic')),
            ],
        ),
    ]
