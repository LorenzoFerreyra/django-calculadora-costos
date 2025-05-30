from django.contrib import admin
from .models import Insumo, Producto, ComponenteProducto
# Register your models here.
admin.site.register(Insumo)
admin.site.register(Producto)
admin.site.register(ComponenteProducto)
