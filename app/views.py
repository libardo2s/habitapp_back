import base64
import re
from django.db.models import Q
from django.core.files.base import ContentFile
from django.db import IntegrityError
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from django.conf.urls.static import static
from django.http import HttpResponse
from rest_framework.decorators import api_view
# Serializers
from .serializerUsuario import UsuarioSerializer
from .serializerInmueble import InmuebleSerializar
from .serializerFotos import FotosSerializer
from .serializerSolicitud import SolicitudSerializar
from .serializerConversacion import ConversacionSerializar
from .serializerComentario import ComentiarioSerializar
from .serializerCiudad import CiudadSerializer
from .serializerUniversidad import UniversidadSerializer
# Models
from django.contrib.auth.models import User
from .models import Usuario, Inmueble, Fotos, SolicitudInmueble, Conversacion, ComentarioValoracion, Ciudad, Universidad


class singIn(APIView):

    def post(self, request, format=None):

        phone = request.data.get('phone') 
        #usr = request.data.get('username')
        #psw = request.data.get('password')
        #user = authenticate(username=usr, password=psw)

        try:
            if Usuario.objects.filter(telefono=phone).exists():
                usuario = Usuario.objects.get(telefono=phone)
                dato = UsuarioSerializer(usuario, many=False)
                response = {
                    'content': dato.data,
                    'isOk': True,
                    'message': ''
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {
                    'content': [],
                    'isOk': False,
                    'message': ''
                }
                return Response(response, status=status.HTTP_200_OK)           
        except Usuario.DoesNotExist:
            response = {
                'content': [],
                'isOk': False,
                'message': 'El usuario no se encuentra registrado',
            }
            return Response(response, status=status.HTTP_200_OK)


class Register(APIView):
    def post(self, request, format=None):
        try:
            name = request.data.get('name')
            lastname = request.data.get('lastname')
            gender = request.data.get('gender')
            age = request.data.get('age')
            city = request.data.get('city')
            university = request.data.get('university')
            is_lessor = request.data.get('lessor')
            phone = request.data.get('phone')
            photo = request.data.get('photo')

            if Usuario.objects.filter(telefono=phone).exists():
                usuario = Usuario.objects.get(telefono=phone)
                dato = UsuarioSerializer(usuario, many=False)
                print(dato.data)
                response = {
                    'content': dato.data,
                    'isOk': True,
                    'message': ''
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                ciudad = Ciudad.objects.get(id=city)
                universidad = Universidad.objects.get(id=university)
                usuario = Usuario.objects.create(
                    nombre=name,
                    apellido=lastname,
                    genero=gender,
                    edad=age,
                    ciudad=ciudad,
                    universidad=universidad,
                    arrendador=is_lessor,
                    telefono=phone
                )
                usuario.save()
                if photo is not None:
                    format, imgstr = photo.split(';base64,')
                    ext = format.split('/')[-1]
                    usuario.foto.save(str(usuario.id)+'.'+ext, ContentFile(base64.b64decode(imgstr)), save=True)
                dato = UsuarioSerializer(usuario, many=False)
                response = {
                    'content': dato.data,
                    'isOk': True,
                    'message': 'Registro exitoso',
                }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e)
            }
            return Response(response, status=status.HTTP_200_OK)


class vivienda(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            vivienda = Inmueble.objects.filter(usuarioInmueble__id=pk)
            dato = InmuebleSerializar(vivienda, many=True)
            response = {
                'content': dato.data,
                'isOk': True,
                'message': '',
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            vivienda = Inmueble.objects.all()  # llama todas las viviendas
            dato = InmuebleSerializar(vivienda, many=True)
            response = {
                'content': dato.data,
                'isOk': True,
                'message': '',
            }
            return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        try:
            ciudad = request.data.get('ciudad')
            idusuario = request.data.get('idusuario')
            foto = request.data.get('foto')
            direccion = request.data.get('direccion')
            barrio = request.data.get('barrio')
            universidad_id = request.data.get('universidad')
            tipovivienda = request.data.get('tipoVivienda')
            precio = request.data.get('precio')
            descripcion = request.data.get('descripcion')
            bano = request.data.get('bano')
            cama = request.data.get('cama')
            wifi = request.data.get('wifi')
            almuerzo = request.data.get('almuerzo')
            accesible = request.data.get('accesible')
            amueblado = request.data.get('amueblado')
            tv = request.data.get('tv')
            lavado = request.data.get('lavado')
            mascota = request.data.get('mascota')
            fumador = request.data.get('fumador')
            piscina = request.data.get('piscina')
            portero = request.data.get('portero')
            camarote = request.data.get('camarote')
            espacio_estudio = request.data.get('espacio_estudio')
            pareja = request.data.get('pareja')
            aire_acondicionado = request.data.get('aire_acondicionado')
            de = request.data.get('de')
            hasta = request.data.get('hasta')
            hombres = request.data.get('hombres')
            mujeres = request.data.get('mujeres')

            images = request.data.get('images')

            usuario = Usuario.objects.get(id=idusuario)
            universidad = Universidad.objects.get(id=universidad_id)

            tipo_vivienda = ''

            if tipovivienda == 0:
                tipo_vivienda = 'Casa'
            elif tipovivienda == 1:
                tipo_vivienda = 'Apartamento'
            elif tipovivienda == 2:
                tipo_vivienda = 'Pensionado'
            elif tipovivienda == 3:
                tipo_vivienda = 'Habitación'
            elif tipovivienda == 3:
                tipo_vivienda = 'Otro'

            inmueble = Inmueble.objects.create(
                usuarioInmueble=usuario, direccion=direccion, barrio=barrio, precio=precio, universidad=universidad,
                tipoVivienda=tipo_vivienda, descripcion=descripcion, bano=bano,  cama=cama, wifi=wifi, almuerzo=almuerzo,
                accesible=accesible, amueblado=amueblado, tv=tv, lavado=lavado, mascota=mascota, fumador=fumador, ciudad=ciudad,
                piscina=piscina, portero=portero, camarote=camarote, espacio_estudio=espacio_estudio, pareja=pareja,
                aire_acondicionado=aire_acondicionado, fechaEntrada=de, fechaSalida=hasta, hombre=hombres, mujeres=mujeres)
            inmueble.save()
            vivienda = Inmueble.objects.filter(usuarioInmueble__id=idusuario)
            
            #imagen_vivienda = Fotos.objects.create(
                #fotos=foto_data,
                #inmuebleFoto=inmueble
            #)
            #imagen_vivienda.save()

            if len(images) < 8:
                for image in images:
                    format, imgstr = image.split(';base64,')
                    ext = format.split('/')[-1]
                    foto_data = ContentFile(base64.b64decode(imgstr), name=inmueble.usuarioInmueble.nombre+'.' + ext)
                    imagen_vivienda = Fotos.objects.create(
                        fotos=foto_data,
                        inmuebleFoto=inmueble
                    )
                    imagen_vivienda.save()

            fotos = Fotos.objects.filter(inmuebleFoto=inmueble.id)
            fotos_dato = FotosSerializer(fotos, many=True)

            dato = InmuebleSerializar(vivienda, many=True)

            response = {
                'content': dato.data,
                'galeria': fotos_dato.data,
                'isOk': True,
                'message': 'Vivienda registrada correctamente',
            }
            return Response(response, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            response = {
                'content': [],
                'isOk': False,
                'message': 'El usuario no se encuentra registrado',
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e),
            }
            return Response(response, status=status.HTTP_200_OK)

    def put(self, request, pk=None, format=None):
        try:
            
            inmueble = Inmueble.objects.get(id=pk)

            regex = re.compile(r'^(?:http|ftp)s?://'  # http:// or https://
                               # domain...
                               r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
                               r'localhost|'  # localhost...
                               r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
                               r'(?::\d+)?'  # optional port
                               r'(?:/?|[/?]\S+)$', re.IGNORECASE)

            foto = request.data.get('foto')
            print(foto)

            if re.match(regex, foto) is None:
                format, imgstr = foto.split(';base64,')
                ext = format.split('/')[-1]
                inmueble.foto.save(inmueble.usuarioInmueble.nombre+'.'+ext,
                                   ContentFile(base64.b64decode(imgstr)), save=True)

            tipovivienda = request.data.get('tipoVivienda')
            tipo_vivienda = ''
            if tipovivienda == 0:
                tipo_vivienda = 'Casa'
            elif tipovivienda == 1:
                tipo_vivienda = 'Apartamento'
            elif tipovivienda == 2:
                tipo_vivienda = 'Pensionado'
            elif tipovivienda == 3:
                tipo_vivienda = 'Habitación'
            elif tipovivienda == 3:
                tipo_vivienda = 'Otro'

            inmueble.tipoVivienda = tipo_vivienda
            inmueble.direccion = request.data.get('direccion')
            inmueble.barrio = request.data.get('barrio')
            #inmueble.universidad = request.data.get('universidad')
            inmueble.precio = request.data.get('precio')
            inmueble.descripcion = request.data.get('descripcion')
            inmueble.bano = request.data.get('bano')
            inmueble.cama = request.data.get('cama')
            inmueble.wifi = request.data.get('wifi')
            inmueble.almuerzo = request.data.get('almuerzo')
            inmueble.accesible = request.data.get('accesible')
            inmueble.amueblado = request.data.get('amueblado')
            inmueble.tv = request.data.get('tv')
            inmueble.lavado = request.data.get('lavado')
            inmueble.mascota = request.data.get('mascota')
            inmueble.fumador = request.data.get('fumador')
            inmueble.piscina = request.data.get('piscina')
            inmueble.portero = request.data.get('portero')
            inmueble.camarote = request.data.get('camarote')
            inmueble.espacio_estudio = request.data.get('espacio_estudio')
            inmueble.pareja = request.data.get('pareja')
            inmueble.aire_acondicionado = request.data.get('aire_acondicionado')
            inmueble.de = request.data.get('de')
            inmueble.hasta = request.data.get('hasta')
            inmueble.hombre = request.data.get('hombres')
            inmueble.mujeres = request.data.get('mujeres')
            inmueble.save()

            serializer = InmuebleSerializar(inmueble, many=False)

            response = {
                'content': serializer.data,
                'isOk': True,
                'message': 'Información actualizada correctamente',
            }
            return Response(response, status=status.HTTP_200_OK)

        except Inmueble.DoesNotExist:
            response = {
                'content': [],
                'isOk': False,
                'message': 'Vivienda no encontrada',
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            response = {
                'content': [],
                'isOk': False,
                'message': str(e),
            }
            return Response(response, status=status.HTTP_200_OK)


class ViviendaEstado(APIView):
    def put(self, request, id=None, format=None):
        try:
            estado = request.data.get('estado')
            estado_data = ''
            if id is not None:
                vivienda = Inmueble.objects.get(id=id)
                if estado == 0:
                    estado_data = 'Disponible'
                elif estado == 1:
                    estado_data = 'Reservado'
                elif estado == 2:
                    estado_data = 'Arrendado'
                vivienda.estado = estado_data
                vivienda.save()

                serializer = InmuebleSerializar(vivienda, many=False)

                response = {
                    'content': serializer.data,
                    'isOk': True,
                    'message': '',
                }
                return Response(response, status=status.HTTP_200_OK)
        except Inmueble.DoesNotExist:
            response = {
                'content': [],
                'isOk': False,
                'message': 'Vivienda no encontrada',
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e),
            }
            return Response(response, status=status.HTTP_200_OK)


class ViviendaImagenes(APIView):
    def put(self, request, id=None, format=None):
        try:
            imagen = request.data.get('image')
            imagen_id = request.data.get('id')
            if id is not None:
                vivienda = Inmueble.objects.get(id=id)
                format, imgstr = imagen.split(';base64,')
                ext = format.split('/')[-1]
                foto_data = ContentFile(base64.b64decode(
                    imgstr), name=vivienda.usuarioInmueble.nombre+'.' + ext)

                if imagen_id == 0:
                    imagen_vivienda = Fotos.objects.create(
                        fotos=foto_data,
                        inmuebleFoto=vivienda
                    )
                    imagen_vivienda.save()
                else:
                    fotos = Fotos.objects.filter(id=imagen_id)
                    fotos[0].fotos.save(vivienda.usuarioInmueble.nombre+'.' + ext,
                                        ContentFile(base64.b64decode(imgstr)), save=True)

                response = {
                    'content': [],
                    'isOk': True,
                    'message': 'Imagen actualizada correctamente',
                }
                return Response(response, status=status.HTTP_200_OK)
        except Inmueble.DoesNotExist:
            response = {
                'content': [],
                'isOk': False,
                'message': 'Vivienda no encontrada',
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e),
            }
            return Response(response, status=status.HTTP_200_OK)


class album(APIView):
    def get(self, request, id=None, format=None):
        if id is None:
            album = Fotos.objects.all()
            dato = FotosSerializer(album, many=True)  # datos que voy a serializar
            response = {
                'content': dato.data,
                'isOk': True,
                'message': '',
            }
        else:
            album = Fotos.objects.filter(inmuebleFoto__id=id, estado=True)  # Filtra una lista por id
            dato = FotosSerializer(album, many=True)
            response = {
                'content': dato.data,
                'isOk': True,
                'message': '',
            }
        return Response(response, status=status.HTTP_200_OK)
    
    def put(self, request, id=None, format=None):
        try:
            images = request.data.get('fotos')
            if id is not None:
                vivienda = Inmueble.objects.get(id=id)
                if len(images) < 8:
                for image in images:
                    format, imgstr = image.split(';base64,')
                    ext = format.split('/')[-1]
                    foto_data = ContentFile(base64.b64decode(imgstr), name=vivienda.usuarioInmueble.nombre+'.' + ext)
                    imagen_vivienda = Fotos.objects.create(
                        fotos=foto_data,
                        inmuebleFoto=vivienda
                    )
                    imagen_vivienda.save()
                
                response = {
                'content': [],
                'isOk': False,
                'message': 'Imagenes creadas correctamente',
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e),
            }
            return Response(response, status=status.HTTP_200_OK)
    
    def delete(self, request, id=None, format=None):
        try:

            if id is not None:
                foto = Fotos.objects.get(id=id)
                foto.estado = False
                foto.save()
                response = {
                'content': [],
                'isOk': False,
                'message': 'Imagen eliminada correctamente',
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e),
            }
            return Response(response, status=status.HTTP_200_OK)


class Solicitud(APIView):
    def get(self, request, id=None, format=None):
        if id is None:
            solicitudes = SolicitudInmueble.objects.all()
            dato = SolicitudSerializar(solicitudes, many=True)
            response = {
                'content': dato.data,
                'isOk': True,
                'message': '',
            }
        else:
            solicitudes = SolicitudInmueble.objects.filter(inmueble__usuarioInmueble__id=id)
            dato = SolicitudSerializar(solicitudes, many=True)
            response = {
                'content': dato.data,
                'isOk': True,
                'message': '',
            }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        try:
            inmueble_id = request.data.get('inmueble')
            usuario_id = request.data.get('usuario')

            solicitud = SolicitudInmueble.objects.filter(
                inmueble__id=inmueble_id, usuario__id=usuario_id)
            if len(solicitud) == 0:
                usuario = Usuario.objects.get(id=usuario_id)
                inmueble = Inmueble.objects.get(id=inmueble_id)

                SolicitudInmueble.objects.create(inmueble=inmueble, usuario=usuario)

                response = {
                    'content': [],
                    'isOk': True,
                    'message': '',
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {
                    'content': [],
                    'isOk': False,
                    'message': 'No hay solicitudes',
                }
                return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e),
            }
            return Response(response, status=status.HTTP_200_OK)

    def delete(self, request, id=None, format=None):
        try:
            solicitud = SolicitudInmueble.objects.get(id=id)
            solicitud.delete()
            response = {
                'content': [],
                'isOk': True,
                'message': 'Solicitud eliminada',
            }
            return Response(response, status=status.HTTP_200_OK)
        except SolicitudInmueble.DoesNotExist:
            response = {
                'content': [],
                'isOk': False,
                'message': 'Solicitud no encontrada',
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e),
            }
            return Response(response, status=status.HTTP_200_OK)


class SolicitudCliente(APIView):
    def get(self, request, id=None, format=None):
        if id is None:
            response = {
                'content': [],
                'isOk': True,
                'message': '',
            }
        else:
            solicitudes = SolicitudInmueble.objects.filter(usuario__id=id)
            dato = SolicitudSerializar(solicitudes, many=True)
            response = {
                'content': dato.data,
                'isOk': True,
                'message': '',
            }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        try:
            inmueble_id = request.data.get('inmueble')
            usuario_id = request.data.get('usuario')
            delete = request.data.get('delete')
            solicitud = SolicitudInmueble.objects.filter(
                inmueble__id=inmueble_id, usuario__id=usuario_id)
            if delete:
                solicitud.delete()
                response = {
                    'content': [],
                    'isOk': True,
                    'message': '',
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                if len(solicitud) > 0:
                    response = {
                        'content': [],
                        'isOk': True,
                        'message': '',
                    }
                else:
                    response = {
                        'content': [],
                        'isOk': False,
                        'message': '',
                    }
                return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e),
            }
            return Response(response, status=status.HTTP_200_OK)


class ConversacionAPIView(APIView):
    def get(self, request, id=None, format=None):
        if id is not None:
            conversaciones = Conversacion.objects.filter(Q(emisor=id) | Q(receptor=id))
            dato = ConversacionSerializar(conversaciones, many=True)
            response = {
                'content': dato.data,
                'isOk': True,
                'message': '',
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                'content': [],
                'isOk': True,
                'message': '',
            }
            return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        try:
            emisor = request.data.get('emisor')
            receptor = request.data.get('receptor')
            conversacionId = request.data.get('conversacion')
            usuario = request.data.get('usuario')

            conversacion = Conversacion.objects.filter(conversacion=conversacionId)

            if len(conversacion) == 0:
                Conversacion.objects.create(
                    usuario=usuario, conversacion=conversacionId, emisor=emisor, receptor=receptor
                )

            response = {
                'content': [],
                'isOk': True,
                'message': '',
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e),
            }
            return Response(response, status=status.HTTP_200_OK)


class PerfilAPi(APIView):
    def get(self, request, id=None, format=None):
        if id is None:
            response = {
                'content': [],
                'isOk': True,
                'message': '',
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            usuario = Usuario.objects.get(id=id)
            dato = UsuarioSerializer(usuario, many=False)
            response = {
                'content': dato.data,
                'isOk': True,
                'message': '',
            }
        return Response(response, status=status.HTTP_200_OK)

    def put(self, request, id=None, format=None):
        try:
            print(request.data)
            nombre = request.data.get('nombre')
            apellido = request.data.get('apellido')
            #correo = request.data.get('correo')
            genero = request.data.get('genero')
            fecha_nacimiento = request.data.get('fechaNacimiento')
            #descripcion = request.data.get('descripcion')
            imagen = request.data.get('imagen')
            arrendador = request.data.get('arrendador')
            #foto = request.data.get('image')

            usuario = Usuario.objects.get(id=id)

            regex = re.compile(r'(?:/?|[/?]\S+)$', re.IGNORECASE)
            
            if re.match(regex, imagen) is None:
                format, imgstr = imagen.split(';base64,')
                ext = format.split('/')[-1]
                usuario.foto.save(usuario.nombre+'_'+str(usuario.id)+'.'+ext,
                                  ContentFile(base64.b64decode(imgstr)), save=True)
            
            usuario.nombre = nombre
            usuario.apellido = apellido
            usuario.arrendador = arrendador
            if genero == 0:
                usuario.genero = 'H'
            else:
                usuario.genero = 'M'
            usuario.edad = fecha_nacimiento
            usuario.save()

            dato = UsuarioSerializer(usuario, many=False)
            response = {
                'content': dato.data,
                'isOk': True,
                'message': '',
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e),
            }
            print(str(e))
            return Response(response, status=status.HTTP_200_OK)


class ComentariosApi(APIView):
    def get(self, request, id=None, format=None):
        try:
            if id is not None:
                comentarios = ComentarioValoracion.objects.filter(inmueble__id=id)
                dato = ComentiarioSerializar(comentarios, many=True)
                response = {
                    'content': dato.data,
                    'isOk': True,
                    'message': '',
                }
            else:
                response = {
                    'content': [],
                    'isOk': False,
                    'message': '',
                }
            return Response(response, status=status.HTTP_200_OK)
        except ComentarioValoracion.DoesNotExist:
            response = {
                'content': [],
                'isOk': False,
                'message': 'Esta vivenda no registra comentarios o valoraciones',
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e),
            }
            return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        print(request.data)
        try:
            idVvivienda = request.data.get('idVvivienda')
            idUsuario = request.data.get('idUsuario')
            comentario = request.data.get('comentario')
            valoracion = request.data.get('valoracion')

            vivienda = Inmueble.objects.get(id=idVvivienda)
            usuario = Usuario.objects.get(id=idUsuario)

            comentario = ComentarioValoracion.objects.create(
                inmueble=vivienda, usuario=usuario, comentario=comentario, valoracion=valoracion)
            dato = ComentiarioSerializar(comentario, many=False)
            response = {
                'content': dato.data,
                'isOk': True,
                'message': 'Comentario exitoso',
            }
            print(dato.data)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e)
            }
            return Response(response, status=status.HTTP_200_OK)


class CiudadApi(APIView):
    def get(self, request, format=None):
        try:
            if id is not None:
                ciudades = Ciudad.objects.all()
                dato = CiudadSerializer(ciudades, many=True)
                response = {
                    'content': dato.data,
                    'isOk': True,
                    'message': '',
                }
            else:
                response = {
                    'content': [],
                    'isOk': False,
                    'message': '',
                }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e),
            }
            return Response(response, status=status.HTTP_200_OK)


class UniversidadApi(APIView):
    def get(self, request, format=None):
        try:
            if id is not None:
                universidades = Universidad.objects.all()
                dato = UniversidadSerializer(universidades, many=True)
                response = {
                    'content': dato.data,
                    'isOk': True,
                    'message': '',
                }
            else:
                response = {
                    'content': [],
                    'isOk': False,
                    'message': '',
                }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e),
            }
            return Response(response, status=status.HTTP_200_OK)


def terminos(request):
    image_data = open(static("Terminos_y_Condiciones.pdf"), ).read()
    return HttpResponse(image_data, mimetype="application/pdf")


@api_view(['GET'])
def obtenerViviendaEstudiante(request, id=None):
    try:
        if id is not None:
            viviendas = Inmueble.objects.filter(universidad__ciudad__id=id)
            dato = InmuebleSerializar(viviendas, many=True)
            response = {
                'content': dato.data,
                'isOk': True,
                'message': '',
            }
            return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        response = {
            'content': [],
            'isOk': False,
            'message': str(e),
        }
        return Response(response, status=status.HTTP_200_OK)
