# Generated by Django 4.2.7 on 2023-12-06 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0005_habilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudios',
            name='estado',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]