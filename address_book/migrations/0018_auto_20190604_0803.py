# Generated by Django 2.2 on 2019-06-04 06:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0017_auto_20190604_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='phone',
            field=models.CharField(blank=True, max_length=50, validators=[django.core.validators.validate_integer]),
        ),
    ]
