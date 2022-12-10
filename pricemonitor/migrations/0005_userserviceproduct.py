# Generated by Django 4.1.3 on 2022-12-06 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pricemonitor', '0004_remove_product_product_url_serviceproduct_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserServiceProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricemonitor.serviceproduct')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
