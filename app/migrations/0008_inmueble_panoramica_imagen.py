# Generated by Django 3.1.1 on 2020-09-09 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_inmueble_panoramica'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='panoramica_imagen',
            field=models.FileField(blank=True, null=True, upload_to='panoramica', verbose_name='Imagen panoramica'),
        ),
    ]