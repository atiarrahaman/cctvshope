# Generated by Django 4.1.4 on 2023-01-04 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0024_remove_placeorder_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeorder',
            name='status',
            field=models.CharField(choices=[('on the way', 'on the way'), ('packed', 'packed'), ('delivered ', 'delivered'), ('cancel ', 'cancel'), ('accepted', 'accepted')], default='Pending', max_length=50),
        ),
    ]
