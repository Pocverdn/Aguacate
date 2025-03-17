
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from main import views as mainViews

urlpatterns = [
    path('', mainViews.index, name="Home"),
    path('metodos/', mainViews.metodos, name="Metodos"),
    path('acercade/', mainViews.acerca_de, name="Acerca de"),
    path('biseccion/', mainViews.biseccion, name="Biseccion"),
    path('reglafalsa/', mainViews.regla_falsa, name="Regla Falsa"),
    path('puntofijo/', mainViews.punto_fijo, name="Punto Fijo"),
    path('newton/', mainViews.newton, name="Newton"),
    path('secante/', mainViews.secante, name="Secante"),
    path('raicesmultiples/', mainViews.raices_multiples, name="Raices Multiples"),
    path('admin/', admin.site.urls),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)