# Generated by Django 4.2.7 on 2023-12-06 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0008_datospersonales_linkedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='datospersonales',
            name='github',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]