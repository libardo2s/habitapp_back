from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.
class Ciudad(models.Model):
    nombre = models.CharField('Nombre', max_length=20)


class Universidad(models.Model):
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    nombre = models.CharField('Nombre', max_length=50)


class Usuario(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField('Nombre', max_length=20)
    apellido = models.CharField('Apellido', max_length=20)
    genero = models.CharField('Genero', max_length=2, null=True)
    edad = models.DateField(null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, null=True, default=1)
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE, null=True, default=1)
    #correo = models.EmailField(unique=True)
    #descripcion = models.CharField('Descripcion', max_length=200, null=True)
    arrendador = models.BooleanField()
    foto = models.ImageField('Foto', upload_to='foto/usuario', null=True)
    telefono = models.CharField('Telefono', max_length=10, unique=True)

    def __str__(self):
        return self.nombre


class Inmueble(models.Model):
    usuarioInmueble = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    ciudad = models.CharField('Ciudad', max_length=100, default='Valledupar')
    def get_usuario_nombre(self):
        return '%s %s' % (self.usuarioInmueble.nombre, self.usuarioInmueble.apellido)
    def get_usuario_telefono(self):
        return self.usuarioInmueble.telefono
    propietario = property(get_usuario_nombre)
    telefono_propietario = property(get_usuario_telefono)
    direccion = models.CharField('Direccion', max_length=50)
    barrio = models.CharField('Barrio', max_length=150)
    precio = models.IntegerField()
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE, null=True)
    tipoVivienda = models.CharField('Vivienda', max_length=15)
    descripcion = models.CharField('Descripcion', max_length=200)
    bano = models.BooleanField()
    cama = models.BooleanField()
    wifi = models.BooleanField()
    almuerzo = models.BooleanField()
    accesible = models.BooleanField()
    amueblado = models.BooleanField()
    tv = models.BooleanField()
    lavado = models.BooleanField()
    mascota = models.BooleanField()
    fumador = models.BooleanField()
    piscina = models.BooleanField()
    portero = models.BooleanField()
    camarote = models.BooleanField()
    espacio_estudio = models.BooleanField()
    pareja = models.BooleanField()
    aire_acondicionado = models.BooleanField()
    fechaEntrada = models.DateField(null=True)
    fechaSalida = models.DateField(null=True)
    instancia = models.IntegerField(null=True)
    hombre = models.IntegerField(null=True)
    mujeres = models.IntegerField(null=True)
    estado = models.CharField('Estado', max_length=15, default='Disponible')
    foto = models.ImageField('Foto', upload_to='foto', null=True)

    def count_comentarios(self):
        return len(ComentarioValoracion.objects.filter(inmueble__id=self.id))

    def avg_valoracion(self):
        try:
            countComentarios = len(ComentarioValoracion.objects.filter(inmueble__id=self.id))
            sumValoraciones = ComentarioValoracion.objects.aggregate(Sum('valoracion'))
            return sumValoraciones.get('valoracion__sum')/countComentarios
        except Exception as e:
            return 0

    valoracionPromedio = property(avg_valoracion)
    comentarios = property(count_comentarios)

    def __str__(self):
        return self.direccion


class Fotos(models.Model):
    fotos = models.ImageField('Foto', upload_to='foto')
    inmuebleFoto = models.ForeignKey(Inmueble, on_delete=models.CASCADE)

    def __str__(self):
        return self.inmuebleFoto.direccion


class SolicitudInmueble(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.inmueble.direccion


class Conversacion(models.Model):
    usuario = models.CharField('Usuario', max_length=100)
    conversacion = models.CharField('Conversacion', max_length=60)
    emisor = models.IntegerField()
    receptor = models.IntegerField()

    def __str__(self):
        return self.usuario


class ComentarioValoracion(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comentario = models.CharField('Comentario', max_length=100)
    valoracion = models.IntegerField()

    def __str__(self):
        return self.usuario.nombre


class Favoritos(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
