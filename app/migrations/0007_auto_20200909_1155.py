# Generated by Django 3.1 on 2020-09-09 16:55

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
        migrations.AddField(
            model_name='inmueble',
            name='panoramica_imagen',
            field=models.FileField(blank=True, null=True, upload_to='panoramica', verbose_name='Imagen panoramica'),
        ),
    ]
