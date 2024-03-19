from django.urls import path

from .views import (
    HotelList,
    HotelDetail
)

urlpatterns=[
    path('hotel/', HotelList.as_view(), name='hotel_list'),
    path('hotel/<int:pk>/', HotelDetail.as_view(), name='hotel_detail')
]