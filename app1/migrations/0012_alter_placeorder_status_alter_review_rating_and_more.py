# Generated by Django 4.1.4 on 2023-01-04 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_alter_placeorder_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeorder',
            name='status',
            field=models.CharField(choices=[('on the way', 'on the way'), ('delivered ', 'delivered'), ('accepted', 'accepted'), ('cancel ', 'cancel'), ('packed', 'packed')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
    ]
