# Generated by Django 3.0.8 on 2020-11-07 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20201107_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='customershop',
        ),
    ]
