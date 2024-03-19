from django.urls import path

from .views import (
    RoomList,
    RoomDetail
)

urlpatterns=[
    path('room/', RoomList.as_view(), name='room_list'),
    path('room/<int:pk>', RoomDetail.as_view(), name='room_detail')
]