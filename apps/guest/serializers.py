from rest_framework.serializers import ModelSerializer

from .models import Guest

class GuestSerializer(ModelSerializer):
    class Meta:
        model=Guest
        fields='__all__'