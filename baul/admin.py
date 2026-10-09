from django.contrib import admin
from .models import Carta, Razon, Cupon, Recuerdo

# Register your models here.
@admin.register(Carta)
class CartaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'icono', 'fecha_creacion')

@admin.register(Razon)
class RazonAdmin(admin.ModelAdmin):
    list_display = ('orden', 'texto')

@admin.register(Cupon)
class CuponAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'canjeado')

@admin.register(Recuerdo)
class RecuerdoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha')