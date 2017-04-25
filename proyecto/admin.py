from django.contrib import admin
from .models import *
# Register your models here.

class OpcionInline(admin.TabularInline):
    model = Opcion
    extra = 4
    min_num = 4
    max_num = 4

@admin.register(Acertijo)
class AcertijoAdmin(admin.ModelAdmin):
    inlines = [OpcionInline,]
    list_display = ('titulo', 'descripcion', 'respuesta', 'respondido')

admin.site.register(Profile)
admin.site.register(Tesoro)
admin.site.register(Medalla)
admin.site.register(Facultad)
