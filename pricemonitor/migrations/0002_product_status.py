# Generated by Django 4.1.3 on 2022-12-01 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricemonitor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('p', 'Oczekuje'), ('r', 'Odrzucone'), ('a', 'Zaakceptowane')], default='p', max_length=1),
        ),
    ]
