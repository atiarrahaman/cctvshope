# Generated by Django 4.1.4 on 2023-01-04 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0033_alter_placeorder_productstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeorder',
            name='productStatus',
            field=models.CharField(choices=[('accepted', 'accepted'), ('on the way', 'on the way'), ('cancel ', 'cancel'), ('packed', 'packed'), ('delivered ', 'delivered')], default='Pending', max_length=50),
        ),
    ]
