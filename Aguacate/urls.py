
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from main import views as mainViews

urlpatterns = [
    path('', mainViews.index, name="Home"),
    path('metodos/', mainViews.metodos, name="Metodos"),
    path('acercade/', mainViews.acercade, name="Acerca de"),
    path('metodo1/', mainViews.metodo1, name="Metodo1"),
    path('metodo2/', mainViews.metodo2, name="Metodo2"),
    path('metodo3/', mainViews.metodo3, name="Metodo3"),
    path('metodo4/', mainViews.metodo4, name="Metodo4"),
    path('metodo5/', mainViews.metodo5, name="Metodo5"),
    path('metodo6/', mainViews.metodo6, name="Metodo6"),
    path('metodo7/', mainViews.metodo7, name="Metodo7"),
    path('metodo8/', mainViews.metodo8, name="Metodo8"),
    path('metodo9/', mainViews.metodo9, name="Metodo9"),
    path('metodo10/', mainViews.metodo10, name="Metodo10"),
    path('metodo11/', mainViews.metodo11, name="Metodo11"),
    path('metodo12/', mainViews.metodo12, name="Metodo12"),
    path('metodo13/', mainViews.metodo13, name="Metodo13"),
    path('metodo14/', mainViews.metodo14, name="Metodo14"),
    path('metodo15/', mainViews.metodo15, name="Metodo15"),
    path('metodo16/', mainViews.metodo16, name="Metodo16"),
    path('metodo17/', mainViews.metodo17, name="Metodo17"),
    path('metodo18/', mainViews.metodo18, name="Metodo18"),
    path('metodo19/', mainViews.metodo19, name="Metodo19"),
    path('metodo20/', mainViews.metodo20, name="Metodo20"),
    path('metodo21/', mainViews.metodo21, name="Metodo21"),
    path('metodo22/', mainViews.metodo22, name="Metodo22"),
    path('metodo23/', mainViews.metodo23, name="Metodo23"),
    path('metodo24/', mainViews.metodo24, name="Metodo24"),
    path('admin/', admin.site.urls),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)