# Generated by Django 4.1.4 on 2023-01-04 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_alter_placeorder_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeorder',
            name='status',
            field=models.CharField(choices=[('delivered ', 'delivered'), ('on the way', 'on the way'), ('accepted', 'accepted'), ('packed', 'packed'), ('cancel ', 'cancel')], default='Pending', max_length=50),
        ),
    ]