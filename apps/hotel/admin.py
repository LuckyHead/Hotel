from django.contrib.admin import *
from .models import Hotel

@register(Hotel)
class HotelAdmin(ModelAdmin):
    list_display=('name', 'rating', 'country', 'city')
    list_display_links=('name', 'rating', 'country', 'city')
    ordering=('-rating',)