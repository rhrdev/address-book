# Generated by Django 2.2 on 2019-06-05 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0018_auto_20190604_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(blank=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
