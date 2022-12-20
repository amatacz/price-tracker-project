# Generated by Django 4.1.3 on 2022-12-19 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricemonitor', '0008_product_product_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=10, verbose_name='Aktualna cena produktu'),
        ),
    ]