# Generated by Django 3.0.6 on 2020-05-13 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='seller',
        ),
    ]