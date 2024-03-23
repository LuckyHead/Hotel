from rest_framework.viewsets import ModelViewSet

from .serializers import HotelSerializer
from .models import Hotel

class HotelListViewSet(ModelViewSet):
    queryset=Hotel.objects.all()
    serializer_class=HotelSerializer

class HotelDetailViewSet(ModelViewSet):
    queryset=Hotel.objects.all()
    serializer_class=HotelSerializer