from django.contrib.admin import *
from .models import Room

@register(Room)
class RoomAdmin(ModelAdmin):
    list_display=('capacity', 'is_used')
    list_display_links=('capacity', 'is_used')
    ordering=('-capacity',)
