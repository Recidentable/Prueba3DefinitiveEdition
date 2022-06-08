from django.urls import path
from .views import Jardineria, Fertilizantes, Flores, Maceteros, registro_usuario, home, form_mod_producto, form_producto, form_del_producto, Tienda

urlpatterns = [
    path('', Jardineria,name="Jardineria"),
    #path('form-del-vehiculo/<id>', form_del_vehiculo, name="form_del_vehiculo"),
    path('form-producto', form_producto, name="form_producto"),
    path('form-mod-producto/<id>', form_mod_producto, name="form_mod_producto"),
    path('form-del-producto/<id>', form_del_producto, name="form_del_producto"),
    path('flores', Flores, name="Flores"),
    path('fertilizantes', Fertilizantes, name="Fertilizantes"),
    path('maceteros', Maceteros, name="Maceteros"),
    path('registro', home, name="home"),
    path('registro-usuario', registro_usuario, name="registro_usuario"),
    path('Tienda', Tienda, name="Tienda"),
]
