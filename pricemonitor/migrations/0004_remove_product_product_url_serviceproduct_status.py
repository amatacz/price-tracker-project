# Generated by Django 4.1.3 on 2022-12-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricemonitor', '0003_service_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_url',
        ),
        migrations.AddField(
            model_name='serviceproduct',
            name='status',
            field=models.CharField(choices=[('p', 'Oczekuje'), ('r', 'Odrzucone'), ('a', 'Zaakceptowane')], default='p', max_length=1),
        ),
    ]
