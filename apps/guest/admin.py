from django.contrib.admin import *
from .models import Guest

@register(Guest)
class UserAdmin(ModelAdmin):
    list_display=('username',)
    list_display_links=('username',)
