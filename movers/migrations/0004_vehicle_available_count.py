# Generated by Django 5.0.1 on 2024-03-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movers', '0003_delete_book_vehicle_vehicle_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='available_count',
            field=models.IntegerField(default=0),
        ),
    ]
