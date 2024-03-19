from rest_framework import generics

from .models import Hotel
from .serializers import HotelSerializer

class HotelList(generics.ListCreateAPIView):
    queryset=Hotel.objects.all()
    serializer_class=HotelSerializer

class HotelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Hotel.objects.all()
    serializer_class=HotelSerializer