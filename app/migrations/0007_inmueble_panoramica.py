# Generated by Django 3.1.1 on 2020-09-09 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_fotos_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='panoramica',
            field=models.BooleanField(default=False),
        ),
    ]
