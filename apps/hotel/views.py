from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet

def homepage(request):
    return render(request, "hotel/home.html")

# class HotelList(LoginRequiredMixin,ListView):
#     model=Hotel
#     template_name="hotel/hotel_list.html"
#     context_object_name='hotels'

# class HotelDetail(DetailView):
#     model=Hotel
#     template_name="hotel/hotel_detail.html"
#     context_object_name="hotel"

def hotel_list(request):
    hotels=Hotel.objects.all()
    context={
        'hotels': hotels
    }
    return render(request, 'hotel/hotel_list.html', context=context)

def hotel_detail(request, pk):
    hotel=Hotel.objects.get(id=pk)
    context={
        'hotel': hotel
    }
    return render(request, 'hotel/hotel_detail.html', context=context)

def hotel_rooms(request, pk):
    if request.user.is_authenticated:
        hotel=Hotel.objects.get(pk=pk)
        rooms=Room.objects.filter(is_used=False, hotel=hotel)
        context = {
            "hotel": hotel,
            "rooms": rooms,
        }
        return render(request, "hotel/hotel_rooms.html",context=context)
    else:
        return redirect("login")

class HotelViewSet(ModelViewSet):
    queryset=Hotel.objects.all()
    serializer_class=HotelSerializer

class RoomViewSet(ModelViewSet):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer

class BookingViewSet(ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer
    