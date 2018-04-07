from django.contrib import admin
from .models import *
# Register your models here.
'''
class OptionInline(admin.TabularInline):
    model = Option
    extra = 4
    min_num = 4
    max_num = 4

@admin.register(Puzzle)
class AcertijoAdmin(admin.ModelAdmin):
    inlines = [OptionInline,]
    list_display = ('name', 'description','medal')
'''
admin.site.register(TypeR)
admin.site.register(TypeT)
admin.site.register(KeyR)
admin.site.register(KeyT)
admin.site.register(Room)
admin.site.register(Treasure)
admin.site.register(Block)
admin.site.register(Medal)
admin.site.register(Mision)
admin.site.register(Department)
admin.site.register(Profile)
admin.site.register(MisionProfile)

