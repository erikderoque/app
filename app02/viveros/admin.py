from django.contrib import admin
from .models import Vivero, Plantas, Cliente, Vendedor, Proveedor

# Register your models here.
admin.site.register(Plantas)
admin.site.register(Vivero)
admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Proveedor)