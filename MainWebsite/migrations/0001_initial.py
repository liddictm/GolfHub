# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-25 17:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0002_auto_20160425_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='GolfEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('location', models.CharField(max_length=1000)),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Users.Groups')),
            ],
        ),
    ]
