# Generated by Django 5.0.1 on 2024-03-03 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movers', '0005_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='available_count',
        ),
    ]
