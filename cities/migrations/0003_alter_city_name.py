# Generated by Django 4.0.4 on 2022-05-28 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_alter_city_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название города'),
        ),
    ]
