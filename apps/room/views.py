from rest_framework.viewsets import ModelViewSet

from .serializers import RoomSerializer
from .models import Room

class RoomListViewSet(ModelViewSet):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer

class RoomDetailViewSet(ModelViewSet):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer