# Generated by Django 3.0 on 2019-12-10 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Conversacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100, verbose_name='Usuario')),
                ('conversacion', models.CharField(max_length=60, verbose_name='Conversacion')),
                ('emisor', models.IntegerField()),
                ('receptor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion')),
                ('barrio', models.CharField(max_length=20, verbose_name='Barrio')),
                ('precio', models.IntegerField()),
                ('universidad', models.CharField(max_length=50, verbose_name='universidad')),
                ('tipoVivienda', models.CharField(max_length=15, verbose_name='Vivienda')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('bano', models.BooleanField()),
                ('cama', models.BooleanField()),
                ('wifi', models.BooleanField()),
                ('almuerzo', models.BooleanField()),
                ('accesible', models.BooleanField()),
                ('amueblado', models.BooleanField()),
                ('tv', models.BooleanField()),
                ('lavado', models.BooleanField()),
                ('mascota', models.BooleanField()),
                ('fumador', models.BooleanField()),
                ('piscina', models.BooleanField()),
                ('portero', models.BooleanField()),
                ('camarote', models.BooleanField()),
                ('espacio_estudio', models.BooleanField()),
                ('pareja', models.BooleanField()),
                ('aire_acondicionado', models.BooleanField()),
                ('fechaEntrada', models.DateField()),
                ('fechaSalida', models.DateField()),
                ('instancia', models.IntegerField(null=True)),
                ('hombre', models.IntegerField(null=True)),
                ('mujeres', models.IntegerField(null=True)),
                ('estado', models.CharField(default='Disponible', max_length=15, verbose_name='Estado')),
                ('foto', models.ImageField(null=True, upload_to='foto', verbose_name='Foto')),
            ],
        ),
        migrations.CreateModel(
            name='Universidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=20, verbose_name='Apellido')),
                ('genero', models.CharField(max_length=2, null=True, verbose_name='Genero')),
                ('edad', models.DateField(null=True)),
                ('arrendador', models.BooleanField()),
                ('foto', models.ImageField(null=True, upload_to='foto/usuario', verbose_name='Foto')),
                ('telefono', models.CharField(max_length=10, unique=True, verbose_name='Telefono')),
                ('ciudad', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Ciudad')),
                ('universidad', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Universidad')),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudInmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Inmueble')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='inmueble',
            name='usuarioInmueble',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Usuario'),
        ),
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotos', models.ImageField(upload_to='foto', verbose_name='Foto')),
                ('inmuebleFoto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Inmueble')),
            ],
        ),
        migrations.CreateModel(
            name='Favoritos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Inmueble')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='ComentarioValoracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=100, verbose_name='Comentario')),
                ('valoracion', models.IntegerField()),
                ('inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Inmueble')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Usuario')),
            ],
        ),
    ]