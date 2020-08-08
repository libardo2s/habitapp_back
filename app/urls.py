from django.urls import path
from .views import singIn, vivienda, album, obtenerViviendaEstudiante, Register, ViviendaEstado, ViviendaImagenes, Solicitud, ConversacionAPIView, PerfilAPi, ComentariosApi, SolicitudCliente, CiudadApi, UniversidadApi, terminos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', singIn.as_view()),
    path('registro/', Register.as_view()),
    path('viviendas/', vivienda.as_view()),
    path('viviendas/estudiante/<int:id>/', obtenerViviendaEstudiante),
    path('viviendas/<int:pk>/', vivienda.as_view()),
    path('viviendas/estado/<int:id>/', ViviendaEstado.as_view()),
    path('viviendas/imagenes/<int:id>/', ViviendaImagenes.as_view()),
    path('fotos/', album.as_view()),
    path('fotos/<int:id>/', album.as_view()),
    path('solicitud/', Solicitud.as_view()),
    path('solicitud/<int:id>/', Solicitud.as_view()),
    path('solicitud/cliente/', SolicitudCliente.as_view()),
    path('cliente/<int:id>/', SolicitudCliente.as_view()),
    path('conversacion/', ConversacionAPIView.as_view()),
    path('conversacion/<int:id>/', ConversacionAPIView.as_view()),
    path('perfil/', PerfilAPi.as_view()),
    path('perfil/<int:id>/', PerfilAPi.as_view()),
    path('comentario/', ComentariosApi.as_view()),
    path('comentario/<int:id>/', ComentariosApi.as_view()),
    path('ciudades/', CiudadApi.as_view()),
    path('universidades/', UniversidadApi.as_view()),
    path('terminosycondiciones/', terminos),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
