# Generated by Django 4.1.4 on 2023-01-04 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0027_alter_placeorder_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placeorder',
            name='status',
        ),
    ]
