from django.contrib.admin import *
from .models import Guest

@register(Guest)
class UserAdmin(ModelAdmin):
    list_display=('username', 'email')
    list_display_links=('username', 'email')
    ordering=('-id',)
    search_fields=('username', 'email', 'first_name', 'last_name')
