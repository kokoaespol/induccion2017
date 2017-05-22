from django.contrib import admin
from .models import *
# Register your models here.

class OptionInline(admin.TabularInline):
    model = Option
    extra = 4
    min_num = 4
    max_num = 4

@admin.register(Puzzle)
class AcertijoAdmin(admin.ModelAdmin):
    inlines = [OptionInline,]
    list_display = ('name', 'description','medal')

admin.site.register(Profile)
#admin.site.register(Puzzle)
admin.site.register(Treasure)
admin.site.register(Medal)
admin.site.register(Department)
admin.site.register(Option)
admin.site.register(Block)
admin.site.register(PuzzleTreasure)
admin.site.register(PuzzleProfile)

