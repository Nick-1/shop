# Generated by Django 3.0.6 on 2020-05-17 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0011_pricesstory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pricesstory',
            options={'ordering': ('-date',)},
        ),
    ]
