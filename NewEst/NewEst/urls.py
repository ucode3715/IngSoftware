from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NewEst.views.home', name='home'),
    # url(r'^blog/', include('blog.urls'))
    url(r'^parametrizar/','estacionamientos.views.parametrizar'),
    url(r'^$','estacionamientos.views.lista_estacionamientos'),
    url(r'^agregar/done','estacionamientos.views.done'),
    url(r'^agregar/','estacionamientos.views.agregar'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reserva/','estacionamientos.views.reserva'),
    url(r'^detalle/','estacionamientos.views.detalle'),
    url(r'^pagar/','estacionamientos.views.pago'),
    url(r'^pagoexitoso/','estacionamientos.views.pagoexitoso'),
)

