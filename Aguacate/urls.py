
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from main import views as mainViews

urlpatterns = [
    path('', mainViews.index, name="Home"),
    path('metodos/', mainViews.metodos, name="Metodos"),
    path('metodo1/', mainViews.metodo1, name="Metodo1"),
    path('metodo2/', mainViews.metodo2, name="Metodo2"),
    path('admin/', admin.site.urls),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)