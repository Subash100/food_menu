# Generated by Django 5.0.7 on 2024-07-22 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='price',
            new_name='item_price',
        ),
    ]
