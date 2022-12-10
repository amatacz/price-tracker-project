# Generated by Django 4.1.3 on 2022-12-07 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pricemonitor', '0005_userserviceproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userserviceproduct',
            name='service_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricemonitor.serviceproduct', unique=True),
        ),
    ]