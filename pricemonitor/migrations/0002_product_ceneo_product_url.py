# Generated by Django 4.1.3 on 2023-01-09 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricemonitor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ceneo_product_URL',
            field=models.CharField(default='brak adresu', max_length=255, verbose_name='Link do ceneo'),
        ),
    ]
