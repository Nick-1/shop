# Generated by Django 3.0.6 on 2020-05-13 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0005_auto_20200511_1723'),
        ('orders', '0006_remove_order_seller'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItems',
            new_name='OrderItem',
        ),
    ]
