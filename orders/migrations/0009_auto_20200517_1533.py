# Generated by Django 3.0.6 on 2020-05-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20200517_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_average_time',
            field=models.DurationField(blank=True, null=True),
        ),
    ]