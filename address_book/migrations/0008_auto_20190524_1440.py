# Generated by Django 2.2 on 2019-05-24 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0007_auto_20190524_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
