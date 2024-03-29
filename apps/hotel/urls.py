from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from .views import HotelViewSet, RoomViewSet, BookingViewSet

router = DefaultRouter()
router.register("hotelapi", HotelViewSet, basename="hotel")
router.register("roomsapi", RoomViewSet, basename="room")
router.register("bookingapi", BookingViewSet, basename="booking")

urlpatterns = [
    path("", homepage, name="home"),
    path("hotels/", HotelList.as_view(), name="hotel_list"),
    path("hotels/<int:pk>/", HotelDetail.as_view(), name="hotel_detail"),
    path("hotels/<int:pk>/rooms/", hotel_rooms, name="hotel_rooms")
]

urlpatterns += router.urls