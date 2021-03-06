# Generated by Django 3.0.6 on 2020-05-11 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopuser', '0002_auto_20200511_1338'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productversion',
            name='sellers',
            field=models.ManyToManyField(related_name='products', to='shopuser.Seller'),
        ),
        migrations.AlterField(
            model_name='section',
            name='sellers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='shopuser.Seller'),
        ),
    ]
