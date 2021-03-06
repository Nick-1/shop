# Generated by Django 3.0.6 on 2020-05-11 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200511_1338'),
        ('shopuser', '0004_address_profile'),
        ('orders', '0002_order_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='shopuser.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('main_sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_items', to='orders.Sale')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='shop.ProductVersion')),
            ],
        ),
    ]
