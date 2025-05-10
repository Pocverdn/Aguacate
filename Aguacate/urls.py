
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from main import views as mainViews
from ec_nl import views as ecViews
from ec_sis import views as ecSViews

urlpatterns = [
    path('', mainViews.index, name="Home"),
    path('metodos/', mainViews.metodos, name="Metodos"),
    path('acercade/', mainViews.acerca_de, name="Acerca de"),
    path('biseccion/', ecViews.biseccion_view, name="Biseccion"),
    path('reglafalsa/', ecViews.regla_falsa, name="Regla Falsa"),
    path('newton/', ecViews.newton, name="Newton"),
    path('secante/', ecViews.secante, name="Secante"),
    path('raicesmultiples/', ecViews.raices_multiples_view, name="Raices Multiples"),
    path('puntofijo/', ecViews.metodo_punto_fijo, name="Punto Fijo"),
    path('jacobi/', ecSViews.jacobi_view, name="Jacobi"),


    path('admin/', admin.site.urls),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)