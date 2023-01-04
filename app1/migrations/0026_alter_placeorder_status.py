# Generated by Django 4.1.4 on 2023-01-04 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_placeorder_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeorder',
            name='status',
            field=models.CharField(choices=[('on the way', 'on the way'), ('accepted', 'accepted'), ('cancel ', 'cancel'), ('packed', 'packed'), ('delivered ', 'delivered')], default='Pending', max_length=50),
        ),
    ]
