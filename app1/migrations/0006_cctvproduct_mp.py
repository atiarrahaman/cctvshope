# Generated by Django 4.1.4 on 2022-12-21 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_megapixel'),
    ]

    operations = [
        migrations.AddField(
            model_name='cctvproduct',
            name='mp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.megapixel'),
        ),
    ]
