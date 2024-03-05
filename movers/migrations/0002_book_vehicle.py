# Generated by Django 5.0.1 on 2024-03-01 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=35)),
                ('Product_type', models.BooleanField()),
                ('Quantity', models.IntegerField()),
                ('Pickup', models.CharField(max_length=40)),
                ('Destination', models.CharField(max_length=40)),
            ],
        ),
    ]