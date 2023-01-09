# Generated by Django 4.1.3 on 2023-01-09 17:38

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import pricemonitor.models.product
import pricemonitor.models.service
import pricemonitor.models.serviceproduct


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255, null=True, verbose_name='Nazwa techniczna')),
                ('verbose_name', models.CharField(max_length=255, null=True, verbose_name='Nazwa produktu')),
                ('status', models.CharField(choices=[('p', 'Oczekuje'), ('r', 'Odrzucone'), ('a', 'Zaakceptowane')], default='p', max_length=1)),
                ('product_URL', models.CharField(default='brak adresu', max_length=255, validators=[pricemonitor.models.product.validate_url], verbose_name='Link do produktu')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=255, validators=[pricemonitor.models.service.validate_url], verbose_name='Adres URL')),
                ('service_name', models.CharField(max_length=30, verbose_name='Nazwa techniczna sklepu')),
                ('verbose_name', models.CharField(max_length=30, verbose_name='Nazwa sklepu')),
                ('status', models.CharField(choices=[('p', 'Oczekuje'), ('r', 'Odrzucone'), ('a', 'Zaakceptowane')], default='p', max_length=1)),
                ('published_data', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_url', models.CharField(default='no address', max_length=255, validators=[pricemonitor.models.serviceproduct.validate_url])),
                ('status', models.CharField(choices=[('p', 'Oczekuje'), ('r', 'Odrzucone'), ('a', 'Zaakceptowane')], default='p', max_length=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricemonitor.product')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='pricemonitor.service')),
            ],
        ),
        migrations.CreateModel(
            name='UserServiceProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed', to='pricemonitor.serviceproduct')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('regular', 'Użytkownik'), ('moderator', 'Moderator')], default='regular', max_length=30)),
                ('avatar', models.ImageField(default='media/default.jpg', null=True, upload_to='static/img/profile_images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProductAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricemonitor.serviceproduct')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='pricemonitor.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProductItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('service_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='pricemonitor.serviceproduct')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProductDataRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField(auto_now_add=True)),
                ('end_datetime', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('e', 'Błąd'), ('p', 'Oczekuje'), ('d', 'Wykonano'), ('r', 'W trakcie')], default='p', max_length=12)),
                ('error_message', models.TextField(default='')),
                ('service_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='pricemonitor.serviceproduct')),
            ],
        ),
    ]
