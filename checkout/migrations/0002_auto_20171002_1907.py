# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-03 02:07
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='number',
            field=models.IntegerField(help_text='Determines the ordering of periods in a day. For example, if Period 4 is given number 4, and Activity 1 is given number 5, then Period 4 occurs right before Activity 1', validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='units',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='sitesku',
            name='units',
            field=models.IntegerField(help_text='Number of units being assigned to this site', validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='week',
            name='week_number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]