from rest_framework.viewsets import ModelViewSet

from .serializers import BookingSerializer
from .models import Booking

class BookingViewSet(ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer

class BookingDetailViewSet(ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer