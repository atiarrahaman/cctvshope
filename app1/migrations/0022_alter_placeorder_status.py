# Generated by Django 4.1.4 on 2023-01-04 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_alter_placeorder_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeorder',
            name='status',
            field=models.CharField(choices=[('packed', 'packed'), ('on the way', 'on the way'), ('cancel ', 'cancel'), ('accepted', 'accepted'), ('delivered ', 'delivered')], default='Pending', max_length=50),
        ),
    ]