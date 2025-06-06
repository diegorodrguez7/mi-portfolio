from django.contrib import admin
from .models import Proyecto, Habilidad, Resumen, Servicio, EntradaBlog

# Register your models here.
@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "fecha_creacion")
    search_fields = ("titulo",)

@admin.register(Habilidad)
class HabilidadAdmin(admin.ModelAdmin):
    list_display = ("nombre", "nivel", "descripcion")
    search_fields = ("nombre",)

@admin.register(Resumen)
class ResumenAdmin(admin.ModelAdmin):
    list_display = ("titulo",)
    search_fields = ("titulo",)

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("titulo",)
    search_fields = ("titulo",)

@admin.register(EntradaBlog)
class EntradaBlogAdmin(admin.ModelAdmin):
    list_display = ("titulo", "fecha_creacion")
    search_fields = ("titulo",)