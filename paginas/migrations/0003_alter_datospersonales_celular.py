# Generated by Django 4.2.7 on 2023-12-05 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0002_datospersonales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datospersonales',
            name='celular',
            field=models.CharField(max_length=20),
        ),
    ]
