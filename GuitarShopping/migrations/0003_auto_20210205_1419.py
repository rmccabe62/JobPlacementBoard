# Generated by Django 2.2.5 on 2021-02-05 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuitarShopping', '0002_auto_20210205_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitar',
            name='price',
            field=models.IntegerField(),
        ),
    ]
