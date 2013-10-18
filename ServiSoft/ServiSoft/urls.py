from django.conf.urls import patterns, include, url
from ServiSoft.views import home
from Telefonia import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ServiSoft.views.home', name='home'),
    # url(r'^ServiSoft/', include('ServiSoft.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^creacioncuenta/$',views.creacion_cuenta),
    url(r'^iniciosesion/$',views.inicio_sesion),
    url(r'^gestionclientes/$',views.gestion_clientes),
    url(r'^creacioncliente/$',views.creacion_cliente),
    url(r'^inicioadmin/$',views.inicio_admin),
    url(r'^modificacioncliente/$',views.modificacion_cliente),
    url(r'^listarclientes/$',views.listar_clientes),
    url(r'^insertarplanes/$',views.insertar_planes),
    url(r'^insercionplanes/$',views.insercion_planes),
    url(r'^insertarservicios/$',views.insertar_servicios),
    url(r'^insercionservicios/$',views.insercion_servicios),
    url(r'^gestionproductos/$',views.gestion_productos),
    url(r'^creacionproducto/$',views.creacion_producto),
    url(r'^afiliarservicio/$',views.afiliar_servicio),
    url(r'^insertarconsumos/$',views.insertar_consumo),
    url(r'^inserciondeconsumo/$',views.insercionde_consumo),
    url(r'^gestionfacturas/$',views.gestion_facturas),
    url(r'^facturarcliente/$',views.facturar_cliente),
    url(r'^facturartodo/$',views.facturar_todo),
    url(r'^consultarultfactura/$',views.consultar_ultfactura),
    url(r'^consultarsaldo/$',views.consultar_saldo),
    url(r'^iniciocliente/$',views.inicio_cliente),
    
)
