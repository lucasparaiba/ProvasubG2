# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-04 23:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transporte_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='atender',
            name='solicitacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transporte_app.Solicitar'),
        ),
    ]