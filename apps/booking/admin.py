from django.contrib.admin import *
from .models import Booking

@register(Booking)
class BookingAdmin(ModelAdmin):
    list_display=('check_in_date',)
    list_display_links=('check_in_date',)