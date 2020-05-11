# Generated by Django 3.0.6 on 2020-05-11 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='OfficeItemProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='office.Office')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_products', to='shop.ProductVersion')),
            ],
        ),
    ]
