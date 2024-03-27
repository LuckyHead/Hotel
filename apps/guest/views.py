from rest_framework.viewsets import ModelViewSet

from .serializers import GuestSerializer
from .models import Guest

class GuestViewSet(ModelViewSet):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer

class GuestDetailViewSet(ModelViewSet):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer